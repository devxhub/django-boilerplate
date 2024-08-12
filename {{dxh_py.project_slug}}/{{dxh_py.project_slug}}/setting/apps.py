from django.apps import AppConfig


class SettingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ dxh_py.project_slug }}.setting'
