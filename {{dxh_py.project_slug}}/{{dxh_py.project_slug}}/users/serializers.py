from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from .models import User

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = ['id', 'email', 'name']