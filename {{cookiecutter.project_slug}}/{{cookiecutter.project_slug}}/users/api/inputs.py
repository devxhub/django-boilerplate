import graphene


class CreateUserInput(graphene.InputObjectType):
    {%- if cookiecutter.username_type == "email" %}
    email = graphene.String()
     {%- else %}
    username = graphene.String()
    {%- endif %}
    password = graphene.String()
    phone_number = graphene.String()

class UpdateUserInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name= graphene.String()
    {%- if cookiecutter.username_type == "email" %}
    email = graphene.String()
    {%- else %}
    username = graphene.String()
    {%- endif %}
