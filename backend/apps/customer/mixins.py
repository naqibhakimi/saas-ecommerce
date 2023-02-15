from apps.core.mutations import Output
from .models import (
    Customer,
    CustomerGroup,
    Country,
    Address,
    Region,
)


class UpdateCustomerMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop('id', None)
        Customer.objects.filter(id = id).update(**kwargs)
        return cls(success= True, errors="")


class UpdateCustomerGroupMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop('id', None)
        CustomerGroup.objects.filter(id = id).update(**kwargs)
        return cls(success = True, errors = "")

        
class UpdateCountryMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop('id', None)
        Country.objects.filter(id = id).update(**kwargs)
        return cls(success = True, errors = "")

        
class UpdateAddressMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop('id', None)
        Address.objects.filter(id = id).update(**kwargs)
        return cls(success = True, errors = "")

        
class UpdateRegionMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop('id', None)
        Region.objects.filter(id = id).update(**kwargs)
        return cls(success = True, errors = "")

        
class CreateAddressMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        pass