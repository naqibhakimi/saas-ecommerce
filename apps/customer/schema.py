from .mutations import UpdateCustomerUpdate

class Query(object):
    pass 

class Mutation(object):
    update_customer = UpdateCustomerUpdate.Field()