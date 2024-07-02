import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from {{ dxh_py.project_slug }}.users.api.filters import UserFilter
User = get_user_model()


class UserObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = User
        fields = ['id', 'name', '{{dxh_py.username_type}}', 'is_active', 'is_staff', 'is_superuser']
        filterset_class = UserFilter
        interfaces = (graphene.relay.Node,)