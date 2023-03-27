import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import (CreateImageMixin, CreatePriceListMixin, CreateProductMixin, CreateProductTagMixin, CreateProductTypeMixin,
                     DeletePriceListMixin, DeleteProductTagMixin, DeleteProductTypeMixin, UpdatePriceListMixin, UpdateProductMixin, DeleteProductMixin, UpdateProductTagMixin, UpdateProductTypeMixin)
from .inputs import (CreateProductInputField, CreateProductTagInputField, UpdateProductInputField, UpdateProductTagInputField, UpdateProductTypeInputField,
                     createPriceListInputField, UpdatePriceListInputField, CreateProductTypeInputField, CreateImageInputField, CreateProductTypeInputField)


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

class UpdatePriceList(DynamicInputMixin, RelayMutationMixin, UpdatePriceListMixin, graphene.ClientIDMutation):
    __doc__ = UpdatePriceListMixin.__doc__
    _inputs = {"price_list": UpdatePriceListInputField}


class DeletePriceList(DynamicInputMixin, RelayMutationMixin, DeletePriceListMixin, graphene.ClientIDMutation):
    __doc__ = DeletePriceListMixin.__doc__
    _required_inputs = {"id": graphene.ID}


class CreateProductType(DynamicInputMixin, RelayMutationMixin, CreateProductTypeMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductTypeMixin.__doc__
    _inputs = {"product_type": CreateProductTypeInputField}


class UpdateProductType(DynamicInputMixin, RelayMutationMixin, UpdateProductTypeMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductTypeMixin.__doc__
    _inputs = {"product_type": UpdateProductTypeInputField}


class DeleteProductType(DynamicInputMixin, RelayMutationMixin, DeleteProductTypeMixin, graphene.ClientIDMutation):
    __doc__ = DeleteProductTypeMixin.__doc__
    _inputs = {"id": graphene.ID()}


class CreateProductTag(DynamicInputMixin, RelayMutationMixin, CreateProductTagMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductTagMixin.__doc__
    _inputs = {"product_tag": CreateProductTagInputField}


class UpdateProductTag(DynamicInputMixin, RelayMutationMixin, UpdateProductTagMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductTagMixin.__doc__
    _inputs = {"product_tag": UpdateProductTagInputField}
    _required_inputs = {}


class DeleteProductTag(DynamicInputMixin, RelayMutationMixin, DeleteProductTagMixin, graphene.ClientIDMutation):
    __doc__ = DeleteProductTagMixin.__doc__
    _required_inputs = {"id": graphene.ID}


class CreateProductImage(DynamicInputMixin, RelayMutationMixin, CreateImageMixin, graphene.ClientIDMutation):
    __doc__ = CreateImageMixin.__doc__
    _inputs = {"image": CreateImageInputField}


class Mutation:
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    create_price_list = CreatePriceList.Field()
    update_price_list = UpdatePriceList.Field()
    delete_price_list = DeletePriceList.Field()
    create_product_type = CreateProductType.Field()
    update_product_type = UpdateProductType.Field()
    delete_product_type = DeleteProductType.Field()
    create_product_tag = CreateProductTag.Field()
    update_product_tag = UpdateProductTag.Field()
    delete_product_tag = DeleteProductTag.Field()
    # create_product_image = CreateProductImage.Field()
