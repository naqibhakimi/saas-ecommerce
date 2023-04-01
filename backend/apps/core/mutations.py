import contextlib
import traceback
from apps.core.types import ExpectedErrorType
import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation, ErrorType
from graphql_relay.node.node import from_global_id

from apps.core.utils.graphql import to_database_id


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
    def convert_to_database_id(cls, kwargs):
        for key, value in kwargs.items():
            with contextlib.suppress(Exception):
                if isinstance(value, dict):
                    cls.convert_to_database_id(value)
                elif isinstance(value, list):
                    for i, k in enumerate(value):
                        value[i] = to_database_id(k)
                kwargs[key] = to_database_id(value)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        cls.convert_to_database_id(kwargs)
        try:
            return cls.resolve_mutation(root, info, **kwargs)
        except Exception as e:
            print(traceback.print_exc())
            return cls(success=False, errors={})

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
                    # TODO: from where this first second ._meta.fields.update comes from?
                    cls._meta.arguments["input"]._meta.fields.update(
                        {key: graphene.InputField(getattr(graphene, cls._inputs[key]))}
                    )
                except Exception:
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
                        {
                            key: graphene.InputField(
                                cls._required_inputs[key], required=True
                            )
                        }
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
