import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import CreateProductMixin, UpdateProductMixin, DeleteProductMixin
from .inputs import CreateProductInputField, UpdateProductInputField


class CreateProduct(DynamicInputMixin, RelayMutationMixin, CreateProductMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductMixin.__doc__
    # [FIXME: What if we need some of required fields as well?]
    _inputs = {"Product": CreateProductInputField}
    _required_inputs = {}


class UpdateProduct(DynamicInputMixin, RelayMutationMixin, UpdateProductMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductMixin.__doc__
    _inputs = {"Product": UpdateProductInputField}
    _required_inputs = {}


class DeleteProduct(DynamicInputMixin, RelayMutationMixin, DeleteProductMixin, graphene.ClientIDMutation):
    __doc__ = DeleteProductMixin.__doc__
    _required_inputs = {"id": graphene.ID}


class Mutation:
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
