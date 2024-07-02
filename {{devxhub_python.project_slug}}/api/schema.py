import graphene
from {{devxhub_python.project_slug}}.users.api.queries import AuthQuery
from {{devxhub_python.project_slug}}.users.api.mutations import AuthMutation


class Query(
        AuthQuery,
        graphene.ObjectType):
    pass


class Mutation(
        AuthMutation,
        graphene.ObjectType):
    pass
