import graphene


class CreateOrUpdateUserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()
