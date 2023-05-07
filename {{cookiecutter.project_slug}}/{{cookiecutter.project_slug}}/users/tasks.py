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
def send_password_reset_otp(email, otp):
    subject = 'Password Reset'
    message = f'Your password reset otp is:  {otp}'
    from_email = env('DEFAULT_FROM_EMAIL')
    to_email = [email]
    send_mail(subject, message, from_email, to_email)