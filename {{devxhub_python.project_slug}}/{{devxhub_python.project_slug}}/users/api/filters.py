from django_filters import *
from {{ devxhub_python.project_slug }}.users.models import User


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
             {%- if devxhub_python.username_type == "email" %}
            'email': ['exact'],
            {%- else %}
            'username': ['exact'],
            {%- endif %}
        }
