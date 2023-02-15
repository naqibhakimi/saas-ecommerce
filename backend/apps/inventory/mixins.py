from apps.core.mutations import Output

class AddressRepository(object):
    def update(self):
        pass

class UpdateAddressMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        AddressRepository().update(root, info, **kwargs)
        return cls(success= True, errors="")