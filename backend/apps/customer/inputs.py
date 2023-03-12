import graphene


class CustomerUpdateInput(graphene.InputObjectType):
    id = graphene.ID(required = True)
    email = graphene.String(required = True)
    billing_address = graphene.ID(required = True)
    phone =  graphene.String()
    first_name =  graphene.String()
    has_account =  graphene.Boolean()
    metadata =  graphene.JSONString()