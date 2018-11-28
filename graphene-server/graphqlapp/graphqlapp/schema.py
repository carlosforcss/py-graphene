import graphene
from users.schema import Query as users_query

class Query(users_query):
    pass

schema = graphene.Schema(query=Query, auto_camelcase=False)
