import graphene

class Output:
    """
    A class to all public classes extend to
    padronize the output
    """

    success = graphene.Boolean(default_value=True)
    errors = graphene.Field(ExpectedErrorType)


class RelayMutationMixin:
    """
    All relay mutations should extend this class
    """
    
    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        return cls.resolve_mutation(root, info, **kwargs)

    @classmethod
    def parent_resolve(cls, root, info, **kwargs):
        return super().mutate_and_get_payload(root, info, **kwargs)


class DynamicInputMixin:
    """
    A class that knows how to initialize graphene relay input

    get inputs from
        cls._inputs
        cls._required_inputs
    inputs is dict { input_name: input_type }
    or list [input_name,] -> defaults to String
    """

    _inputs = {}
    _required_inputs = {}

    @classmethod
    def Field(cls, *args, **kwargs):
        if isinstance(cls._inputs, dict):
            for key in cls._inputs:
                try:
                    cls._meta.arguments["input"]._meta.fields.update(
                        {key: graphene.InputField(getattr(graphene, cls._inputs[key]))}
                    )
                except:
                    cls._meta.arguments["input"]._meta.fields.update(
                        {key: graphene.InputField(cls._inputs[key])}
                    )
        elif isinstance(cls._inputs, list):
            for key in cls._inputs:
                cls._meta.arguments["input"]._meta.fields.update(
                    {key: graphene.InputField(graphene.String)}
                )

        if isinstance(cls._required_inputs, dict):
            for key in cls._required_inputs:
                if not isinstance(cls._required_inputs[key], str):
                    cls._meta.arguments["input"]._meta.fields.update(
                        {key: graphene.InputField(cls._required_inputs[key])}
                    )
                else:
                    cls._meta.arguments["input"]._meta.fields.update(
                        {
                            key: graphene.InputField(
                                getattr(graphene, cls._required_inputs[key]),
                                required=True,
                            )
                        }
                    )
        elif isinstance(cls._required_inputs, list):
            for key in cls._required_inputs:
                cls._meta.arguments["input"]._meta.fields.update(
                    {key: graphene.InputField(graphene.String, required=True)}
                )
        return super().Field(*args, **kwargs)
