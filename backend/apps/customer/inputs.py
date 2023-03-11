import graphene


class CustomerUpdateInput(graphene.InputObjectType):
    billing_address = graphene.String(required = True)
    hone =  graphene.String()
    as_account =  graphene.String()
    assword_hash =  graphene.String()
    rder =  graphene.String()
    roups =  graphene.String()
    metadata =  graphene.JSONString()