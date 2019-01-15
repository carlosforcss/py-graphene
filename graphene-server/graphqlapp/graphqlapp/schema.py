import graphene
from users.schema import Query as users_query
from users.schema import Mutations as users_mutations

class Query(users_query):
    pass

class Mutations(users_mutations):
    pass

schema = graphene.Schema(query=Query, mutation = Mutations, auto_camelcase=False)
