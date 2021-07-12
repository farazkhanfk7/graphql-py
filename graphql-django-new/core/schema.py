import graphene
from graphene_django import DjangoObjectType
import graphene_django
from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id","title","body")

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root, info, **kwargs):
        return Book.objects.all()

schema = graphene.Schema(query=Query)