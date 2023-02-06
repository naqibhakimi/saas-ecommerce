import graphene
class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True
