from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
import graphql
from . import views
from . schema import schema

urlpatterns = [
    path('',views.home,name="home"),
    path('graphql',GraphQLView.as_view(graphiql=True,schema=schema))
]