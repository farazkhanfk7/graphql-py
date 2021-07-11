import json
import graphene
from datetime import datetime
from graphene import Schema

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)

class Query(graphene.ObjectType):
    users = graphene.List(User, num=graphene.Int(default_value=3))

    def resolve_users(self,info, num):
        return [
            User(username='Alice',last_login=datetime.now()),
            User(username='Faraz',last_login=datetime.now()),
            User(username='Aquib',last_login=datetime.now()),
        ][:num]

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
    
    user = graphene.Field(User)

    def mutate(self,info,username):
        if info.context.get('vip'):
            username = username.upper()

        user = User(username=username)
        return CreateUser(user=user)

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = Schema(query=Query, mutation=Mutations)

my_query = """
{
    users (num: 3){
        username
        lastLogin
    }
}
"""

mutation_query = """
mutation createUser($username: String) {
    createUser(username : $username){
        user {
            username
        }
    }
}
"""
result = schema.execute(mutation_query, variable_values={'username':'Nikhil'},context={'vip':False})
data = dict(result.data.items())

print(json.dumps(data, indent=3))