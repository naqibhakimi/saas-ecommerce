from apps.core.types import ExpectedErrorType
import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation, ErrorType
from graphql_relay.node.node import from_global_id

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



class AbstractMutation(DjangoModelFormMutation):

    # @classmethod
    # def mutate_and_get_payload(cls, root, info, **input):
    #     form = cls.get_form(root, info, **input)

    #     if form.is_valid():
    #         return cls.perform_mutate(form, info)
    #     else:
    #         errors = ErrorType.from_errors(form.errors)

    #         return cls(errors=errors)

    # @classmethod
    # def get_form_kwargs(cls, root, info, **input):
    #     kwargs = {"data": input}

    #     pk = input.pop("id", None)
    #     if pk:
    #         _, pk = from_global_id(pk)
    #         instance = cls._meta.model._default_manager.get(pk=pk)
    #         kwargs["instance"] = instance

    #     return kwargs

    class Meta:
        abstract = True



class DynamicArgsMixin:
    """
    A class that knows how to initialize graphene arguments
    get args from
        cls._args
        cls._required_args
    args is dict { arg_name: arg_type }
    or list [arg_name,] -> defaults to String
    """

    _args = {}
    _required_args = {}

    @classmethod
    def Field(cls, *args, **kwargs):
        if isinstance(cls._args, dict):
            for key in cls._args:
                cls._meta.arguments.update(
                    {key: graphene.Argument(getattr(graphene, cls._args[key]))}
                )
        elif isinstance(cls._args, list):
            for key in cls._args:
                cls._meta.arguments.update({key: graphene.String()})

        if isinstance(cls._required_args, dict):
            for key in cls._required_args:
                cls._meta.arguments.update(
                    {
                        key: graphene.Argument(
                            getattr(graphene, cls._required_args[key]), required=True
                        )
                    }
                )
        elif isinstance(cls._required_args, list):
            for key in cls._required_args:
                cls._meta.arguments.update({key: graphene.String(required=True)})
        return super().Field(*args, **kwargs)
