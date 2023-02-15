import graphene


class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True


class TaxLineConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class TaxRateConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class TaxProviderConnection(BaseConnection):
    class Meta:
        abstract = True 

        
