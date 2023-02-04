import graphene


class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True


class AnalyticsConfigConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class BatchJobConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class FulfillmentConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class FulfillmentItemConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class FulfillmentProviderConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class TrackingLinkConnection(BaseConnection):
    class Meta:
        abstract = True 

        
