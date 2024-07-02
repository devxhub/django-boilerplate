import graphene
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth import get_user_model
from {{ dxh_py.project_slug }}.users.api.schema import UserObjectType
User = get_user_model()


class AuthQuery(graphene.ObjectType):
    users = DjangoFilterConnectionField(UserObjectType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


user_schema_query = graphene.Schema(query=AuthQuery)
