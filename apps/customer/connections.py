import graphene


class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True


class CustomerConnection(BaseConnection):
    class Meta:
        abstract = True
class CustomerGroupConnection(BaseConnection):
    class Meta:
        abstract = True
class CountryConnection(BaseConnection):
    class Meta:
        abstract = True
class AddressConnection(BaseConnection):
    class Meta:
        abstract = True
class RegionConnection(BaseConnection):
    class Meta:
        abstract = True