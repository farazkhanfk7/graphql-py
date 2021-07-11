import json
import graphene
from datetime import datetime
from graphene import Schema

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime()

class Query(graphene.ObjectType):
    users = graphene.List(User, num=graphene.Int(default_value=3))

    def resolve_users(self,info, num):
        return [
            User(username='Alice',last_login=datetime.now()),
            User(username='Faraz',last_login=datetime.now()),
            User(username='Aquib',last_login=datetime.now()),
        ][:num]

schema = Schema(query=Query)

my_query = """
{
    users (num: 1){
        username
        lastLogin
    }
}
"""
result = schema.execute(my_query)
data = dict(result.data.items())

print(json.dumps(data, indent=3))