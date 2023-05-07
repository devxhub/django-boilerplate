import graphene
from api.schema import *


schema = graphene.Schema(query=Query, mutation=Mutation)