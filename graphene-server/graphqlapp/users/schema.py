from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import graphene
from graphene_django.types import DjangoObjectType
from .models import Message


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ('password')

class MessageType(DjangoObjectType):
    class Meta:
        model = Message

class LoginType(UserType):
    password = graphene.String()
    class Meta:
         model = User
         exclude_fields = ('password', )


class UserInputs(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)

class CreateUser(graphene.Mutation):
    class Input:
        name = graphene.String(required=False)

    class Arguments: 
        username = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    def mutate(self, info, username, password, first_name, last_name):
        User.objects.create_user(username = username,
                            password = password,
                            first_name = first_name,
                            last_name = last_name)
        user = UserType(username=username)
        ok = True
        return CreateUser(user = user, ok = ok)



class Query(graphene.ObjectType):
    users = graphene.List(UserType, )
    messages = graphene.List(MessageType)
    login = graphene.Boolean(username = graphene.String(), password = graphene.String())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_messages(self, info, **kwargs):
        return Message.objects.all()

    def resolve_login(self, info, username, password, **kwargs):
        if authenticate(username=username, password=password):
            return True
        else:
            return False

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()