from rest_framework import serializers

from {{ dxh_py.project_slug }}.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        {%- if dxh_py.username_type == "email" %}
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }
        {%- else %}
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }
        {%- endif %}
