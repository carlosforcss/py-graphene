import graphene
import json
import datetime

'''
==================
    OBJECTS
==================
'''

# Users 
class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)

'''
==================
    DEFINE MUTACIONES
==================
'''

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
    user = graphene.Field(User)

    def mutate(self, info, username):
        if info.context.get('is_vip'):
            username = username.upper()
        user = User(username=username)
        return CreateUser(user=user)


'''
==================
    RUTAS DE LA QUERY
==================
'''

class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        print('resolve start')
        return [
            User(username='Carlos', last_login=datetime.datetime.now()),
            User(username='David', last_login=datetime.datetime.now()),
            User(username='ASDFASDF', last_login=datetime.datetime.now()),
            User(username='asdfasdf', last_login=datetime.datetime.now()),
            User(username='asdfasdf', last_login=datetime.datetime.now())
        ][:first]


''' DEFINIR LAS MUTACIONES '''
class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=False)

result = schema.execute(
    '''
    mutation my_mutation($username: String) {
        create_user(username: $username){
            user {
                username
            }
        }
    }
    ''',
    variable_values = {
        'username': 'Alice'
    },
    context={'is_vip': True}
)

items = result.data

print(json.dumps(items, indent=4))
