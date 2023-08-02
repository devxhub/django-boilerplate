from django.contrib.auth.models import AbstractUser
from django.db.models import CharField{% if cookiecutter.username_type == "email" %}, EmailField{% endif %}
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
{%- if cookiecutter.username_type == "email" %}

from {{ cookiecutter.project_slug }}.users.managers import UserManager
{%- endif %}


class User(AbstractUser):
    """
    Default custom user model for {{cookiecutter.project_name}}.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    reset_password_token = models.CharField(max_length=255, blank=True, null=True)
    reset_otp= models.CharField(max_length=6, blank=True, null=True)
    verify_token = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    phone_verified = models.BooleanField(default=False)
    {%- if cookiecutter.username_type == "email" %}
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    {%- endif %}

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        {%- if cookiecutter.username_type == "email" %}
        return reverse("users:detail", kwargs={"pk": self.id})
        {%- else %}
        return reverse("users:detail", kwargs={"username": self.username})
        {%- endif %}

class PhoneVerification(models.Model):
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    otp = models.CharField(max_length=4, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.phone_number