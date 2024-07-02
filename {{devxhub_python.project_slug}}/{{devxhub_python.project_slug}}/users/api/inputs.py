import graphene


class CreateUserInput(graphene.InputObjectType):
    {%- if devxhub_python.username_type == "email" %}
    email = graphene.String()
     {%- else %}
    username = graphene.String()
    {%- endif %}
    password = graphene.String()

class UpdateUserInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name= graphene.String()
    {%- if devxhub_python.username_type == "email" %}
    email = graphene.String()
    {%- else %}
    username = graphene.String()
    {%- endif %}
