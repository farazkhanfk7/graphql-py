import graphene
from graphene import Schema

data = [
    {
        "f_name":"Faraz",
        "age":"22"
    },
    {
        "f_name":"Chetan",
        "age":"23"
    }
]

class Person(graphene.ObjectType):
    f_name = graphene.String()
    age = graphene.String()


class Query(graphene.ObjectType):
    array = graphene.List(Person)

    def resolve_array(root, info):
        return data

schema = Schema(query=Query)
# use auto_camelcase = False to avoid it.  

print(schema)

print("==============================")

# use fName ( f_name to fName )
query_graphql = """
query myquery {
    array {
        fName
    }
}
"""

result = schema.execute(query_graphql)
print(result)