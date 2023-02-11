from django.conf import settings
import graphene
import graphene_django_optimizer as gql_optimizer
from graphene_django.utils import camelize
from graphql.error import GraphQLLocatedError
from apps.core.ratelimit import ratelimit
from apps.auth.exceptions import WrongUsage
import base64
import collections

import graphene
from graphene_django import converter, utils

from .utils import check_id

    
class ExpectedErrorType(graphene.Scalar):
    class Meta:
        description = """
    Errors messages and codes mapped to
    fields or non fields errors.
    Example:
    {
        field_name: [
            {
                "message": "error message",
                "code": "error_code"
            }
        ],
        other_field: [
            {
                "message": "error message",
                "code": "error_code"
            }
        ],
        nonFieldErrors: [
            {
                "message": "error message",
                "code": "error_code"
            }
        ]
    }
    """

    @staticmethod
    def serialize(errors):
        if isinstance(errors, dict):
            if errors.get("__all__", False):
                errors["non_field_errors"] = errors.pop("__all__")
            return camelize(errors)
        elif isinstance(errors, list):
            return {"nonFieldErrors": errors}
        raise WrongUsage("`errors` must be list or dict!")


class Output:
    """
    A class to all public classes extend to
    padronize the output
    """

    success = graphene.Boolean(default_value=True)
    errors = graphene.Field(ExpectedErrorType)


class Node:
    @classmethod
    def get_queryset(cls, queryset, info):
        return gql_optimizer.query(queryset, info)

    @classmethod
    def get_node(cls, info, id):
        queryset = cls.get_queryset(cls._meta.model.objects, info)
        try:
            return queryset.get(pk=check_id(id))
        except cls._meta.model.DoesNotExist as e:
            raise GraphQLLocatedError(
                nodes=[],
                original_error=e,
            )

    @classmethod
    def get_node_by_parameters(cls, info, **kwargs):
        queryset = cls.get_queryset(cls._meta.model.objects, info)
        try:
            return queryset.get(**kwargs)
        except cls._meta.model.DoesNotExist as e:
            raise GraphQLLocatedError(
                nodes=[],
                original_error=e,
            )


class RelayMutationMixin:
    """
    All relay mutations should extend this class
    """

    
    @classmethod
    @ratelimit(key="ip", rate=settings.RATE_LIMIT_MUTATION, block=True)
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



def check_id(id):
    if not id:
        return None

    if isinstance(id, str):
        if str(id).isnumeric():
            return int(id)
        value = base64.urlsafe_b64decode(id).decode()
        value = int(value.split(":")[1])
        return int(value)
    else:
        return int(id)


def convert_fields(model, only_fields=[], except_fields=[]):
    model_fields = utils.get_model_fields(model=model)
    fields = collections.OrderedDict()

    for name in only_fields:
        if name.endswith("__id"):
            fields[name] = graphene.ID(required=False)

    for field in model_fields:
        name, d_type = field

        # Must be in only_fields
        if only_fields and name not in only_fields:
            continue

        if name in except_fields:
            continue

        if name.endswith("__id"):
            continue

        if name == "id":
            fields[name] = graphene.ID(required=False)
            continue

        converted = converter.convert_django_field(d_type, None)

        if not converted:
            continue

        fields[name] = converted

    return fields
