import graphene


class CreateUserInput(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()

class UpdateUserInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name= graphene.String()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()
