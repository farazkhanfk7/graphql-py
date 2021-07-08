import graphene
from graphene import Schema

data = [
    {
        "name":"Faraz",
        "age":"22"
    },
    {
        "name":"Chetan",
        "age":"23"
    }
]

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()


class Query(graphene.ObjectType):
    array = graphene.List(Person)

    def resolve_array(root, info):
        return data

schema = Schema(query=Query)

print(schema)

print("==============================")

query_graphql = """
query myquery {
    array {
        name
    }
}
"""

result = schema.execute(query_graphql)
print(result)