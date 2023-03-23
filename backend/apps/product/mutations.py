import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import CreatePriceListMixin, CreateProductMixin, DeletePriceListMixin, UpdatePriceListMixin, UpdateProductMixin, DeleteProductMixin
from .inputs import CreateProductInputField, UpdateProductInputField, createPriceListInputField, UpdatePriceListInputField


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


class CreatePriceList(DynamicInputMixin, RelayMutationMixin, CreatePriceListMixin, graphene.ClientIDMutation):
    __doc__ = CreatePriceListMixin.__doc__
    _inputs = {"price_list": createPriceListInputField}
    # [FIXME: HOW we can put in a LIST]
    # _inputs = [createPriceListInputField]


class UpdatePriceList(DynamicInputMixin, RelayMutationMixin, UpdatePriceListMixin, graphene.ClientIDMutation):
    __doc__ = UpdatePriceListMixin.__doc__
    _inputs = {"price_list": UpdatePriceListInputField}


class DeletePriceList(DynamicInputMixin, RelayMutationMixin, DeletePriceListMixin, graphene.ClientIDMutation):
    __doc__ = DeletePriceListMixin.__doc__
    _required_inputs = {"id": graphene.ID}


class Mutation:
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    create_price_list = CreatePriceList.Field()
    update_price_list = UpdatePriceList.Field()
    delete_price_list = DeletePriceList.Field()
