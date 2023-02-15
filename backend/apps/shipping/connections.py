import graphene


class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True


class ShippingProfileTypeConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class ShippingProfileConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class ShippingOptionConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class ShippingMethodConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class CustomShippingOptionConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class ShippingMethodTaxLineConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class ShippingOptionRequirementConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class ShippingTaxRateConnection(BaseConnection):
    class Meta:
        abstract = True 

        
