from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from {{ cookiecutter.project_slug }}.users.forms import UserAdminChangeForm, UserAdminCreationForm
from {{ cookiecutter.project_slug }}.users.models import PhoneVerification
User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        {%- if cookiecutter.username_type == "email" %}
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        {%- else %}
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        {%- endif %}
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["{{cookiecutter.username_type}}", "name", "is_superuser", "is_active","phone_verified"]
    search_fields = ["name"]
    {%- if cookiecutter.username_type == "email" %}
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    {%- endif %}


class PhoneVerificationAdmin(admin.ModelAdmin):
    list_display = ['id','phone_number', 'otp','expires_at']
    search_fields = ['phone_number', 'otp']
   

admin.site.register(PhoneVerification, PhoneVerificationAdmin)