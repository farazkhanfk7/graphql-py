import graphene
from snippets.schema import SnippetQuery

class Query(SnippetQuery):
    pass

schema = graphene.Schema(query=Query)