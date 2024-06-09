from django.conf import settings
{%- if cookiecutter.use_twillio == 'y' %}
from twilio.rest import Client
{%- endif %}
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from config import celery_app
import environ
from django.template.loader import render_to_string

env = environ.Env()
User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@shared_task
def send_password_reset_email(email, token):
    token_url = f'{env("FRONTEND_URL")}/reset-password/{token}'
    # context = {
    #     'token_url': token_url,
    # }
    subject = 'Password Reset'
    # html_message = render_to_string('users/password_reset_email.html', context)
    message = f'Your password reset token is {token_url}'
    from_email = env('DEFAULT_FROM_EMAIL')
    to_email = [email]
    send_mail(subject, message, from_email, to_email)


@shared_task
def send_account_confirmation_email(email, verify_token):
    token_url = f'{env("FRONTEND_URL")}/verify-email/{verify_token}'
    subject = 'Confirm your email'
    from_email = env('DEFAULT_FROM_EMAIL')
    message = f"Please confirm your email {token_url}"
    send_mail(subject, message, from_email, [email], fail_silently=False)
    return True


@shared_task
def send_password_reset_otp(email, otp):
    subject = 'Password Reset'
    message = f'Your password reset otp is:  {otp}'
    from_email = env('DEFAULT_FROM_EMAIL')
    to_email = [email]
    send_mail(subject, message, from_email, to_email)



{%- if cookiecutter.use_twillio == 'y' %}
@shared_task
def send_sms(to_phone_number, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        messaging_service_sid=settings.TWILIO_SERVICE_SID,
        to=to_phone_number
    )
    return message.sid
{%- endif %}



{%- if cookiecutter.use_twillio == 'n' %}
@shared_task
def send_sms(to_phone_number, message):
    return True

{%- endif %}