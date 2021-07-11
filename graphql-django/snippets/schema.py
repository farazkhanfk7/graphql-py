import graphene
from graphene_django import DjangoObjectType
from .models import Snippet

class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet

class SnippetQuery(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)

    def resolve_all_snippets(self,info, **kwargs):
        return Snippet.objects.all()