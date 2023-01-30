import graphene

class Query(graphene.ObjectType):
    test = graphene.String()

class Mutatation(graphene.ObjectType):
     test_object = graphene.String()

class Subscription(graphene.ObjectType):
    test = graphene.String()

schema = graphene.Schema(query=Query, mutation=Mutatation, subscription=Subscription)