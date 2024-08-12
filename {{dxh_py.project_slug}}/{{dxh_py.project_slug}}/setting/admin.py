from django.contrib import admin
from {{ dxh_py.project_slug }}.setting.models import PasswordPolicies, SystemConfiguration


class PasswordPoliciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_length', 'min_uppercase', 'min_lowercase', 'min_numerals', 'min_special_chars')


class SystemConfigurationAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'date_format', 'timezone', 'time_format', 'currency', 'created_at', 'updated_at')
    list_filter = ('timezone', 'currency', 'date_format', 'time_format')


admin.site.register(PasswordPolicies, PasswordPoliciesAdmin)
admin.site.register(SystemConfiguration, SystemConfigurationAdmin)