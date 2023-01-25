import graphene

class AddressConnection(graphene.Connection):
    class Meta:
        abstract = True