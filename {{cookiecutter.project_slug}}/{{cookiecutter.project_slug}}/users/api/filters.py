from django_filters import *
from {{ cookiecutter.project_slug }}.users.models import User


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
             {%- if cookiecutter.username_type == "email" %}
            'email': ['exact'],
            {%- else %}
            'username': ['exact'],
            {%- endif %}
        }
