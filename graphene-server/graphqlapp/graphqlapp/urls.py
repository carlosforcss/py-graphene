from django.contrib import admin
from graphene_django.views import GraphQLView
from django.urls import path
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(
        graphiql=True,
        schema=schema
    ))
]
