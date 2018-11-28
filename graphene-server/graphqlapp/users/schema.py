from django.contrib.auth.models import User as UserModel
import graphene
from graphene_django import DjangoObjectType

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolver_users(self, info, **kwargs):
        return UserModel.objects.all()
