import graphene
from graphene import Schema

class Query(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()

    def resolve_name(root, info):
        return "Faraz"
    def resolve_age(root, info):
        return 22

schema = Schema(query=Query)

print(schema)

print("==============================")

query_graphql = """
query myquery {
    name
    age
}
"""

result = schema.execute(query_graphql)
print(result)