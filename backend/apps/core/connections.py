import graphene
class BaseConnection(graphene.Connection):
    find = graphene.String()

    def resolve_find(root, info, **kwargs):
        print(root)
    
    class Meta:
        abstract = True
