import graphene
import graphql_jwt
import string
import random
import environ
from graphql import GraphQLError
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token
from {{ cookiecutter.project_slug }}.users.api.inputs import CreateOrUpdateUserInput
from {{ cookiecutter.project_slug }}.users.api.schema import UserObjectType
{%- if cookiecutter.use_celery == 'y' %}
from {{ cookiecutter.project_slug }}.users.tasks import send_password_reset_email, send_password_reset_otp
{%- endif %}
{%- if cookiecutter.use_celery == 'n' %}
from django.template.loader import render_to_string
{%- endif %}


env = environ.Env()
User = get_user_model()


class CreateOrUpdateUser(graphene.Mutation):
    user = graphene.Field(UserObjectType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        input = CreateOrUpdateUserInput(required=True)

    def mutate(self, info, input):
        user = User.objects.filter(email=input.email).first()
        if user:
            if input.password:
                user.set_password(input.password)
            if input.username:
                user.username = input.username
            user.save()
        else:
            user = User.objects.create_user(
                email=input.email,
                password=input.password,
                username=input.username,
            )
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateOrUpdateUser(user=user, token=token, refresh_token=refresh_token)


class SendPasswordResetEmailMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(self, info, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return SendPasswordResetEmailMutation(success=False)
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        {%- if cookiecutter.use_celery == 'y' %}
        
        send_password_reset_email.delay(email, token)
        {%- else %}
        token_url = f'{env("FRONTEND_URL")}/reset-password/{token}'
        subject = 'Password Reset'
        message = f'Your password reset token is {token_url}'
        from_email = env('DEFAULT_FROM_EMAIL')
        to_email = [email]
        send_mail(subject, message, from_email, to_email)
        
        {%- endif %}
        
        user.reset_password_token = token
        user.save()
        return SendPasswordResetEmailMutation(success=True)


class ResetPasswordMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        new_password = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, token, new_password):
        try:
            user = User.objects.get(reset_password_token=token)
        except User.DoesNotExist:
            return ResetPasswordMutation(success=False)
        user.set_password(new_password)
        user.reset_password_token = None
        user.save()

        return ResetPasswordMutation(success=True)



class SendPasswordResetOTP(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(self, info, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return SendPasswordResetOTP(success=False)
        otp= ''.join(random.choices(string.digits, k=6))
        {%- if cookiecutter.use_celery == 'y' %}
        send_password_reset_otp.delay(email, otp)
        {%- else %}
        subject = 'Password Reset OTP'
        message = f'Your password reset otp is:  {otp}'
        from_email = env('DEFAULT_FROM_EMAIL')
        to_email = [email]
        send_mail(subject, message, from_email, to_email)
        {%- endif %}
        user.reset_otp=otp 
        user.save()
        return SendPasswordResetOTP(success=True)



class VerifyPasswordResetOTP(graphene.Mutation):
    class Arguments:
        new_password = graphene.String(required=True)
        otp = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, otp, new_password):
        try:
            user = User.objects.get(reset_otp=otp)
        except User.DoesNotExist:
            return VerifyPasswordResetOTP(success=False)
        user.set_password(new_password)
        user.reset_otp = None
        user.save()
        return VerifyPasswordResetOTP(success=True)
       


class AuthMutation(graphene.ObjectType):
    create_or_update_user = CreateOrUpdateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()
    send_password_reset_email = SendPasswordResetEmailMutation.Field()
    reset_password = ResetPasswordMutation.Field()
    send_password_reset_otp = SendPasswordResetOTP.Field()
    verify_password_reset_otp = VerifyPasswordResetOTP.Field()


user_schema_mutation = graphene.Schema(mutation=AuthMutation)