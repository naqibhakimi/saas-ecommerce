import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import (CreateImageMixin, CreateMoneyAmountMixin, CreatePriceListMixin, CreateProductCategoryMixin, CreateProductCollectionMixin, CreateProductMixin, CreateProductOptionMixin, CreateProductOptionValueMixin, CreateProductTagMixin, CreateProductTaxRateMixin, CreateProductTypeMixin, DeleteImageMixin, DeleteMoneyAmountMixin,
                     DeletePriceListMixin, DeleteProductCategoryMixin, DeleteProductCollectionMixin, DeleteProductOptionMixin, DeleteProductOptionValueMixin, DeleteProductTagMixin, DeleteProductTaxRateMixin, DeleteProductTypeMixin, UpdateImageMixin, UpdateMoneyAmountMixin,
                     UpdatePriceListMixin, UpdateProductCategoryMixin, UpdateProductCollectionMixin, UpdateProductMixin, DeleteProductMixin, UpdateProductOptionMixin, UpdateProductOptionValueMixin, UpdateProductTagMixin, UpdateProductTaxRateMixin, UpdateProductTypeMixin)
from .inputs import (CreateMoneyAmountInputField, CreateProductInputField, CreateProductOptionValueInputField, CreateProductTagInputField, CreateProductTypeTaxRateInputField, UpdateImageInputField,
                     UpdateProductCategoryInputField, UpdateProductCollectionInputField,
                     UpdateProductInputField, UpdateProductTagInputField, UpdateProductTaxRateInputField, UpdateProductTypeInputField,
                     createPriceListInputField, UpdatePriceListInputField, CreateProductTypeInputField,
                     CreateImageInputField, CreateProductTypeInputField, CreateProductCollectionInputField,
                     UpdateMoneyAmountInputField, CreateProductCategoryInputField,
                     CreateProductOptionInputField, UpdateProductOptionInputField,
                     UpdateProductOptionValueInputField, CreateProductTaxRateInputField)


class CreateProduct(DynamicInputMixin, RelayMutationMixin, CreateProductMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductMixin.__doc__
    _inputs = {"Product": CreateProductInputField}
    # This way it will make the product itself as required
    # _required_inputs = {"Product": CreateProductInputField}


class UpdateProduct(DynamicInputMixin, RelayMutationMixin, UpdateProductMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductMixin.__doc__
    _inputs = {"Product": UpdateProductInputField}


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
    # TODO: MAKE THIS ID REQUIRED IN DELETE IN ALL APPS
    _inputs = {"id": graphene.ID}


class CreateMoneyAmount(DynamicInputMixin, RelayMutationMixin, CreateMoneyAmountMixin, graphene.ClientIDMutation):
    __doc__ = CreateMoneyAmountMixin.__doc__
    _inputs = {"money_amount": CreateMoneyAmountInputField}


class UpdateMoneyAmount(DynamicInputMixin, RelayMutationMixin, UpdateMoneyAmountMixin, graphene.ClientIDMutation):
    __doc__ = UpdateMoneyAmountMixin.__doc__
    _inputs = {"money_amount": UpdateMoneyAmountInputField}


class DeleteMoneyAmount(DynamicInputMixin, RelayMutationMixin, DeleteMoneyAmountMixin, graphene.ClientIDMutation):
    __doc__ = DeleteMoneyAmountMixin.__doc__
    _inputs = {"id": graphene.ID}


class CreateProductCategory(DynamicInputMixin, RelayMutationMixin, CreateProductCategoryMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductCategoryMixin.__doc__
    _inputs = {"product_category": CreateProductCategoryInputField}


class UpdateProductCategory(DynamicInputMixin, RelayMutationMixin, UpdateProductCategoryMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductCategoryMixin.__doc__
    _inputs = {"product_category": UpdateProductCategoryInputField}


class DeleteProductCategory(DynamicInputMixin, RelayMutationMixin, DeleteProductCategoryMixin, graphene.ClientIDMutation):
    __doc__ = DeleteProductCategoryMixin.__doc__
    _inputs = {"id": graphene.ID}


class CreateProductOption(DynamicInputMixin, RelayMutationMixin, CreateProductOptionMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductOptionMixin.__doc__
    _inputs = {"product_option": CreateProductOptionInputField}


class UpdateProductOption(DynamicInputMixin, RelayMutationMixin, UpdateProductOptionMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductOptionMixin.__doc__
    _inputs = {"product_option": UpdateProductOptionInputField}


class DeleteProductOption(DynamicInputMixin, RelayMutationMixin, DeleteProductOptionMixin, graphene.ClientIDMutation):
    __doc__ = DeleteProductOptionMixin.__doc__
    _inputs = {"id": graphene.ID}


class CreateProductOptionValue(DynamicInputMixin, RelayMutationMixin, CreateProductOptionValueMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductOptionValueMixin.__doc__
    _inputs = {"product_option_value": CreateProductOptionValueInputField}


class UpdateProductOptionValue(DynamicInputMixin, RelayMutationMixin, UpdateProductOptionValueMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductOptionValueMixin.__doc__
    _inputs = {"product_option_value": UpdateProductOptionValueInputField}


class DeleteProductOptionValue(DynamicInputMixin, RelayMutationMixin, DeleteProductOptionValueMixin, graphene.ClientIDMutation):
    __doc__ = DeleteProductOptionValueMixin.__doc__
    _inputs = {"id": graphene.ID}


class CreateProductTaxRate(DynamicInputMixin, RelayMutationMixin, CreateProductTaxRateMixin, graphene.ClientIDMutation):
    __doc__ = CreateProductTaxRateMixin.__doc__
    _inputs = {"product_tax_rate": CreateProductTaxRateInputField}


class UpdateProductTaxRate(DynamicInputMixin, RelayMutationMixin, UpdateProductTaxRateMixin, graphene.ClientIDMutation):
    __doc__ = UpdateProductTaxRateMixin.__doc__
    _inputs = {"product_tax_rate": UpdateProductTaxRateInputField}


class DeleteProductTaxRate(DynamicInputMixin, RelayMutationMixin, DeleteProductTaxRateMixin, graphene.ClientIDMutation):
    __doc__ = DeleteProductTaxRateMixin.__doc__
    _inputs = {"id": graphene.ID}


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
    update_money_amount = UpdateMoneyAmount.Field()
    delete_money_amount = DeleteMoneyAmount.Field()
    create_product_category = CreateProductCategory.Field()
    update_product_category = UpdateProductCategory.Field()
    delete_product_category = DeleteProductCategory.Field()
    create_product_option = CreateProductOption.Field()
    update_product_option = UpdateProductOption.Field()
    delete_product_option = DeleteProductOption.Field()
    create_product_option_value = CreateProductOptionValue.Field()
    update_product_option_value = UpdateProductOptionValue.Field()
    delete_product_option_value = DeleteProductOptionValue.Field()
    create_product_tax_rate = CreateProductTaxRate.Field()
    update_product_tax_rate = UpdateProductTaxRate.Field()
    delete_product_tax_rate = DeleteProductTaxRate.Field()
    # TODO :  permission: admin, customer, staff --> MAKE DECORATOR
    # resolve mutation ---> decorator should be apply on top of
    # auth make permission a custom permission
