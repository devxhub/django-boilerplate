from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from {{ dxh_py.project_slug }}.models import BaseModel
from {{ dxh_py.project_slug }}.utils.constants import DATE_FORMAT_CHOICES, CURRENCY_CHOICES, TIMEZONES, TIME_FORMAT_CHOICES


class PasswordPolicies(BaseModel):
    id = models.BigAutoField(primary_key=True)
    min_length = models.IntegerField(default=4, blank=True, null=True)
    min_uppercase = models.IntegerField(default=1, blank=True, null=True)
    min_lowercase = models.IntegerField(default=1, blank=True, null=True)
    min_numerals = models.IntegerField(default=1, blank=True, null=True)
    min_special_chars = models.IntegerField(default=1, blank=True, null=True)
    password_hint =  models.TextField(verbose_name=_('Password Hint'), blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    def clean(self):
        super().clean()
        min_uppercase = self.min_uppercase or 0
        min_lowercase = self.min_lowercase or 0
        min_numerals = self.min_numerals or 0
        min_special_chars = self.min_special_chars or 0
        min_length = self.min_length or 0
        
        total_length = min_uppercase + min_lowercase + min_numerals + min_special_chars
        
        if total_length > min_length:
            raise ValidationError(
                "The sum of minimum uppercase, lowercase, numerals, and special characters cannot exceed the minimum length."
            )


class SystemConfiguration(BaseModel):
    date_format = models.CharField(
        max_length=20, 
        choices=DATE_FORMAT_CHOICES, 
        default='MM/DD/YYYY'
    )
    timezone = models.CharField(
        max_length=50, 
        choices=TIMEZONES, 
        default='UTC'
    )
    time_format = models.CharField(
        max_length=20, 
        choices=TIME_FORMAT_CHOICES, 
        default='HH:MM AM/PM'
    )
    decimal_places = models.PositiveIntegerField(default=2)
    login_attempts = models.PositiveIntegerField(default=5)
    two_factor_authentication = models.BooleanField(default=False)
    currency = models.CharField(
        max_length=10, 
        choices=CURRENCY_CHOICES, 
        default='USD'
    )

    def __str__(self):
        return f"System Configuration {self.uuid}"

    class Meta:
        verbose_name = 'System Configuration'
        verbose_name_plural = 'System Configurations'