import graphene
import graphql_jwt
import string
import random
import environ
import pytz
from datetime import datetime, timedelta
from graphql import GraphQLError
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token
from {{ cookiecutter.project_slug }}.users.models import *
from {{ cookiecutter.project_slug }}.users.api.inputs import *
from {{ cookiecutter.project_slug }}.users.api.schema import UserObjectType
{%- if cookiecutter.use_celery == 'y' %}
from {{ cookiecutter.project_slug }}.users.tasks import *
{%- endif %}
{%- if cookiecutter.use_celery == 'n' %}
from django.template.loader import render_to_string
{%- endif %}

env = environ.Env()
User = get_user_model()



class TokenAuthMutation(graphql_jwt.ObtainJSONWebToken):
    user = graphene.Field(UserObjectType)
    token = graphene.String()
    refresh_token = graphene.String()

    @classmethod
    def resolve(cls, root, info, **kwargs):
        user = info.context.user
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return cls(user=user, token=token, refresh_token=refresh_token)

class CreateUserMutation(graphene.Mutation):
    class Arguments:
        input = CreateUserInput(required=True)

    user = graphene.Field(UserObjectType)
    token = graphene.String()
    refresh_token = graphene.String()
    verify_token = graphene.String()

    def mutate(self, info, input):
        user = User.objects.create_user(
            {%- if cookiecutter.username_type == "email" %}
            email=input.email,
            {%- else %}
            username=input.username,
            {%- endif %}
            phone_number=input.phone_number,
            password=input.password,
            is_active=False,
        )
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        verify_token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        user.verify_token = verify_token
        user.save()
        otp = random.randint(1111, 9999)

        PhoneVerification.objects.create(
            otp=otp,
            phone_number=user.phone_number,
            expires_at=datetime.now(
                tz=pytz.utc) + timedelta(seconds=120)
        )
        message = f"{otp} is your OTP to verify your phone number. This OTP is valid for 2 minutes"
        send_sms.delay(user.phone_number, message)

        {%- if cookiecutter.use_celery == 'y' %}
        send_account_confirmation_email.delay(input.email, verify_token)
        {%- else %}
        token_url = f'{env("FRONTEND_URL")}/verify-email/{verify_token}'
        subject = 'Confirm your email'
        from_email = env('DEFAULT_FROM_EMAIL')
        message = f"Please confirm your email {token_url}"
        to_email = [input.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        {%- endif %}
        return CreateUserMutation(user=user, token=token, refresh_token=refresh_token)

class PhoneVerificationSMS(graphene.Mutation):
    class Arguments:
        phone_number = graphene.String(required=True)
        otp = graphene.String(required=True)

    success = graphene.Boolean()
    user = graphene.Field(UserObjectType)
    token = graphene.String()
    refresh_token = graphene.String()

    def mutate(self, info, phone_number, otp):
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise GraphQLError('User does not exist')
       
        try:
            phone_verification = PhoneVerification.objects.get(
                phone_number=user.phone_number,
                otp=otp  
            )
            if phone_verification.expires_at < datetime.now(tz=pytz.utc):
                raise GraphQLError('OTP has expired')

        except Exception as e:
            raise GraphQLError(e)
        phone_verification.delete()
        user.is_active = True
        user.phone_verified = True
        user.save()
        return PhoneVerificationSMS(success=True, user=user, token=get_token(user), refresh_token=create_refresh_token(user))


class UpdateUserMutation(graphene.Mutation):
    user = graphene.Field(UserObjectType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        input = UpdateUserInput()
    success = graphene.Boolean()

    @staticmethod
    def mutate(self, info, input):
        try:
            user = User.objects.get(id=input.id)
        except User.DoesNotExist:
            raise GraphQLError('User does not exist')
        {%- if cookiecutter.username_type == "email" %}
        if input.email:
            user.email = input.email
        {%- else %}
        if input.username:
            user.username = input.username
        {%- endif %}
        if input.name:
            user.name = input.name
        if input.password:
            user.set_password(input.password)
        user.save()
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return UpdateUserMutation(user=user, token=token, refresh_token=refresh_token, success=True)


class DeleteUserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise GraphQLError('User does not exist')
        user.delete()
        return DeleteUserMutation(success=True)


class SendConfirmationEmailMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise GraphQLError('User does not exist')
        verify_token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        {%- if cookiecutter.use_celery == 'y' %}
        send_account_confirmation_email.delay(input.email, verify_token)
        {%- else %}
        token_url = f'{env("FRONTEND_URL")}/verify-email/{verify_token}'
        subject = 'Confirm your email'
        from_email = env('DEFAULT_FROM_EMAIL')
        message = f"Please confirm your email {token_url}"
        to_email = [input.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        {%- endif %}
        user.verify_token = verify_token
        user.save()
        return SendConfirmationEmailMutation(success=True)


class VerifyAccountMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, token):
        try:
            user = User.objects.get(verify_token=token)
        except User.DoesNotExist:
            return VerifyAccountMutation(success=False)
        user.is_active = True
        user.verify_token = None
        user.save()

        return VerifyAccountMutation(success=True)
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
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
    delete_user = DeleteUserMutation.Field()
    token_auth = TokenAuthMutation.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()
    send_password_reset_email = SendPasswordResetEmailMutation.Field()
    reset_password = ResetPasswordMutation.Field()
    verify_account_token = VerifyAccountMutation.Field()
    verify_account_sms = PhoneVerificationSMS.Field()
    send_confirmation_email = SendConfirmationEmailMutation.Field()
    send_password_reset_otp = SendPasswordResetOTP.Field()
    verify_password_reset_otp = VerifyPasswordResetOTP.Field()


user_schema_mutation = graphene.Schema(mutation=AuthMutation)