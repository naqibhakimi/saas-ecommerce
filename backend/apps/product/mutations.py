import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import (CreateImageMixin, CreateMoneyAmountMixin, CreatePriceListMixin, CreateProductCollectionMixin, CreateProductMixin, CreateProductTagMixin, CreateProductTypeMixin, DeleteImageMixin,
                     DeletePriceListMixin, DeleteProductCollectionMixin, DeleteProductTagMixin, DeleteProductTypeMixin, UpdateImageMixin,
                     UpdatePriceListMixin, UpdateProductCollectionMixin, UpdateProductMixin, DeleteProductMixin, UpdateProductTagMixin, UpdateProductTypeMixin)
from .inputs import (CreateMoneyAmountInputField, CreateProductInputField, CreateProductTagInputField, UpdateImageInputField, UpdateProductCollectionInputField, UpdateProductInputField, UpdateProductTagInputField, UpdateProductTypeInputField,
                     createPriceListInputField, UpdatePriceListInputField, CreateProductTypeInputField, CreateImageInputField, CreateProductTypeInputField, CreateProductCollectionInputField)


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


class UpdateProductImage(DynamicInputMixin, RelayMutationMixin, UpdateImageMixin, graphene.ClientIDMutation):
    __doc__ = UpdateImageMixin.__doc__
    _inputs = {"image": UpdateImageInputField}


class DeleteProductImage(DynamicInputMixin, RelayMutationMixin, DeleteImageMixin, graphene.ClientIDMutation):
    __doc__ = DeleteImageMixin.__doc__
    _inputs = {"id": graphene.ID}


class CreateProductCollection(DynamicInputMixin, RelayMutationMixin, CreateProductCollectionMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductCollectionMixin.__doc__
    _inputs = {"collection": CreateProductCollectionInputField}


class UpdateProductCollection(DynamicInputMixin, RelayMutationMixin, UpdateProductCollectionMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductCollectionMixin.__doc__
    _inputs = {"collection": UpdateProductCollectionInputField}


class DeleteProductCollection(DynamicInputMixin, RelayMutationMixin, DeleteProductCollectionMixin, graphene.ClientIDMutation):
    __doc__ = DeleteProductCollectionMixin.__doc__
    # FIXME: Whey here we use just ID but in inputs we use ID()
    _inputs = {"id": graphene.ID}


class CreateMoneyAmount(DynamicInputMixin, RelayMutationMixin, CreateMoneyAmountMixin, graphene.ClientIDMutation):
    __doc__ = CreateMoneyAmountMixin.__doc__
    _inputs = {"money_amount": CreateMoneyAmountInputField}


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
    create_product_image = CreateProductImage.Field()
    update_product_image = UpdateProductImage.Field()
    delete_product_image = DeleteProductImage.Field()
    create_product_collection = CreateProductCollection.Field()
    update_product_collection = UpdateProductCollection.Field()
    delete_product_collection = DeleteProductCollection.Field()
    create_money_amount = CreateMoneyAmount.Field()
