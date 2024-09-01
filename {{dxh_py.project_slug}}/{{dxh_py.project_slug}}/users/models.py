{%- if dxh_py.username_type == "email" %}
from typing import ClassVar
{% endif -%}
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
{%- if dxh_py.username_type == "email" %}
from django.db.models import EmailField
{%- endif %}
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
{%- if dxh_py.username_type == "email" %}

from .managers import UserManager
{%- endif %}


class User(AbstractUser):
    """
    Default custom user model for {{dxh_py.project_name}}.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    
    # Overriding fields in AbstractUser
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    
    {%- if dxh_py.username_type == "email" %}
    username = None  # type: ignore
    {%- endif %}

    # Custom fields
    name = CharField(_("Name of User"), blank=True, max_length=255)
    reset_password_token = CharField(max_length=255, blank=True, null=True)
    reset_otp= CharField(max_length=6, blank=True, null=True)
    verify_token = CharField(max_length=255, blank=True, null=True)
    {%- if dxh_py.username_type == "email" %}
    email = EmailField(_("email address"), unique=True)

    # Update the USERNAME_FIELD and REQUIRED_FIELDS
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects: ClassVar[UserManager] = UserManager()
    {%- endif %}

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        {%- if dxh_py.username_type == "email" %}
        return reverse("users:detail", kwargs={"pk": self.id})
        {%- else %}
        return reverse("users:detail", kwargs={"username": self.username})
        {%- endif %}