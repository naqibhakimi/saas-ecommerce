from apps.core.mutations import Output


class UpdateAddressMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        return cls(success=True, errors="")
