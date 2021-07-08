import graphene
from graphene import Schema

class Query(graphene.ObjectType):
    name = graphene.String(name=graphene.String(default_value="Person"))
    age = graphene.String()

    def resolve_name(root, info, name):
        return f"Hello {name}"
    def resolve_age(root, info):
        return 22

schema = Schema(query=Query)

print(schema)

print("==============================")

query_graphql = """
query myquery {
    name (name: "Faraz")
    age
}
"""

result = schema.execute(query_graphql)
print(result)