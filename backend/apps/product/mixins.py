from apps.core.mutations import Output
from django.forms import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .forms import (CreateImageForm, CreateMoneyAmountForm, CreatePriceListFrom,
                    CreateProductCategoryForm, CreateProductCollectionForm, CreateProductFrom,
                    CreateProductOptionForm, CreateProductOptionValueForm,
                    CreateProductTagForm, CreateProductTaxRateForm, CreateProductTypeTaxRateForm,
                    CreateProductVariantForm, CreateVariantInventoryItemForm,
                    UpdateImageForm, UpdatePriceListForm,
                    UpdateProductCollectionForm, UpdateProductFrom,
                    CreateProductTypeForm, UpdateProductTagForm, UpdateProductTypeForm,
                    UpdateVariantInventoryItemForm, UpdateProductTypeTaxRateForm,
                    UpdateMoneyAmountForm, UpdateMoneyAmountForm,
                    UpdateProductCategoryForm, UpdateProductOptionForm,
                    UpdateProductOptionValueForm, UpdateProductTaxRateForm,
                    UpdateVariantInventoryItemForm, UpdateProductVariantForm
                    )
from .constant import Message
from .models import Image, MoneyAmount, PriceList, Product, ProductCategory, ProductCollection, ProductOption, ProductOptionValue, ProductTag, ProductTaxRate, ProductType, ProductTypeTaxRate, ProductVariant, ProductVariantInventoryItem


class CreateProductMixin(Output):
    form = CreateProductFrom

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs.get("Product", None))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.PRODUCT_CREATED)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class UpdateProductMixin(Output):
    form = UpdateProductFrom

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        product_data = kwargs.get("Product")
        try:
            form = cls.form(data=product_data, instance=Product.objects.get(
                id=product_data.pop("id")))
            if form.is_valid():
                # for many to many
                tags = product_data.pop("tags")
                images = product_data.pop("images")
                sales_channels = product_data.pop("sales_channels")
                instance = form.save(commit=False)
                instance.save(update_fields=product_data.keys())
                instance.tags.set(tags, clear=True)
                instance.images.set(images, clear=True)
                instance.sales_channels.set(sales_channels, clear=True)
                return cls(success=True, errors=Message.PRODUCT_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class DeleteProductMixin(Output):

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            # [FIXME: filter or get]
            Product.objects.filter(id=kwargs.get("id")).delete()
            return cls(success=True, errors=Message.PRODUCT_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.PRODUCT_NOT_FOUND)


class CreatePriceListMixin(Output):
    form = CreatePriceListFrom

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs.get("price_list"))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.PRICE_LIST_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdatePriceListMixin(Output):
    form = UpdatePriceListForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        price_list_data = kwargs.get("price_list")
        try:
            form = cls.form(data=kwargs.get("price_list"),
                            instance=PriceList.objects.get(id=price_list_data.pop('id')))
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields=price_list_data.keys())
                return cls(success=True, errors=Message.PRICE_LIST_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class DeletePriceListMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            # [FIXME: it should be all get not filter to avoid api fetch problem]
            PriceList.objects.get(id=kwargs.get("id", None)).delete()
            return cls(success=True, errors=Message.PRICE_LIST_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.PRICE_LIST_NOT_FOUND)


class CreateProductTypeMixin(Output):
    form = CreateProductTypeForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs.get('product_type'))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.PRODUCT_TYPE_CREATED)
            return cls(success=False, errors=form.errors)

        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductTypeMixin(Output):
    form = UpdateProductTypeForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        product_type_data = kwargs.get('product_type')
        try:
            form = cls.form(data=product_type_data, instance=ProductType.objects.get(
                id=product_type_data.pop('id')))
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields=product_type_data.keys())
                return cls(success=True, errors=Message.PRODUCT_TYPE_UPDATED)
            return cls(success=False, errors=form.errors)

        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=form.errors)


class DeleteProductTypeMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            ProductType.objects.get(id=kwargs.get("id")).delete()
            return cls(success=True, errors=Message.PRODUCT_TYPE_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.PRODUCT_TYPE_NOT_EXIST)


class CreateProductTagMixin(Output):
    form = CreateProductTagForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        product_tag_data = kwargs.get("product_tag")
        try:
            form = cls.form(data=product_tag_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.PRODUCT_TAG_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductTagMixin(Output):
    form = UpdateProductTagForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        product_tag_date = kwargs.get("product_tag")
        try:
            form = cls.form(data=product_tag_date,
                            instance=ProductTag.objects.get(id=product_tag_date.pop('id')))
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields=product_tag_date.keys())
                return cls(success=True, errors=Message.PRODUCT_TAG_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class DeleteProductTagMixin(Output):

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            ProductTag.objects.get(id=kwargs.get('id')).delete()
            return cls(success=True, errors=Message.PRODUCT_TAG_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.PRODUCT_TAG_NOT_FOUND)


class CreateImageMixin(Output):
    form = CreateImageForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        image_data = kwargs.get("image")
        try:
            form = cls.form(data=image_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.PRODUCT_IMAGE_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateImageMixin(Output):
    form = UpdateImageForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        image_data = kwargs.get("image")
        try:
            form = cls.form(data=image_data, instance=Image.objects.get(
                id=image_data.pop("id")))
            if form.is_valid():
                instance = form.save(commit=False)
                # FIXME: how do you use (update_fields) and where actually it is?
                # inside save we have only one argument which is commit so where this update_fields
                instance.save(update_fields=image_data.keys())
                return cls(success=True, errors=Message.PRODUCT_IMAGE_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class DeleteImageMixin(Output):

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            Image.objects.get(id=kwargs.get('id')).delete()
            return cls(success=True, errors=Message.Image_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.PRODUCT_IMAGE_NOT_FOUND)


class CreateProductCollectionMixin(Output):
    form = CreateProductCollectionForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        product_collection_data = kwargs.get("collection")
        try:
            form = cls.form(data=product_collection_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.PRODUCT_COLLECTION_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductCollectionMixin(Output):
    form = UpdateProductCollectionForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        product_collection_data = kwargs.get("collection")
        try:
            form = cls.form(data=product_collection_data,
                            instance=ProductCollection.objects.get(id=product_collection_data.pop('id')))
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields=product_collection_data.keys())
                return cls(success=True, errors=Message.PRODUCT_COLLECTION_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class DeleteProductCollectionMixin(Output):

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            ProductCollection.objects.get(id=kwargs.get('id')).delete()
            return cls(success=True, errors=Message.PRODUCT_COLLECTION_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.PRODUCT_COLLECTION_NOT_FOUND)


class CreateMoneyAmountMixin(Output):
    #   TODO: explaining the whole form
    form = CreateMoneyAmountForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        money_amount_data = kwargs.get("money_amount")
        try:
            form = cls.form(data=money_amount_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.MoneyAmount_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateMoneyAmountForm(Output):
    form = UpdateMoneyAmountForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        MoneyAmount_data = kwargs.get("MoneyAmount")
        try:
            form = cls.form(data=MoneyAmount.objects.get(id=MoneyAmount_data.pop("id")))
            if form.is_error:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields="")
                return cls(success=True, errors=Message.asdf_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class CreateProductCategoryMixin(Output):
    form = CreateProductCategoryForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductCategory_data = kwargs.get("ProductCategory")
        try:
            form = cls.form(data=ProductCategory_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.ProductCategory_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductCategoryForm(Output):
    form = UpdateProductCategoryForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductCategory_data = kwargs.get("ProductCategory")
        try:
            form = cls.form(data=ProductCategory.objects.get(
                id=ProductCategory_data.pop("id")))
            if form.is_error:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields="")
                return cls(success=True, errors=Message.asdf_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class CreateProductOptionMixin(Output):
    form = CreateProductOptionForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductOption_data = kwargs.get("ProductOption")
        try:
            form = cls.form(data=ProductOption_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.ProductOption_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductOptionForm(Output):
    form = UpdateProductOptionForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductOption_data = kwargs.get("ProductOption")
        try:
            form = cls.form(data=ProductOption.objects.get(
                id=ProductOption_data.pop("id")))
            if form.is_error:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields="")
                return cls(success=True, errors=Message.asdf_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class CreateProductOptionValueMixin(Output):
    form = CreateProductOptionValueForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductOptionValue_data = kwargs.get("ProductOptionValue")
        try:
            form = cls.form(data=ProductOptionValue_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.ProductOptionValue_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductOptionValueForm(Output):
    form = UpdateProductOptionValueForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductOptionValue_data = kwargs.get("ProductOptionValue")
        try:
            form = cls.form(data=ProductOptionValue.objects.get(
                id=ProductOptionValue_data.pop("id")))
            if form.is_error:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields="")
                return cls(success=True, errors=Message.asdf_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class CreateProductTaxRateMixin(Output):
    form = CreateProductTaxRateForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductTaxRate_data = kwargs.get("ProductTaxRate")
        try:
            form = cls.form(data=ProductTaxRate_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.ProductTaxRate_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductTaxRateForm(Output):
    form = UpdateProductTaxRateForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductTaxRate_data = kwargs.get("ProductTaxRate")
        try:
            form = cls.form(data=ProductTaxRate.objects.get(
                id=ProductTaxRate_data.pop("id")))
            if form.is_error:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields="")
                return cls(success=True, errors=Message.asdf_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class CreateProductTypeTaxRateMixin(Output):
    form = CreateProductTypeTaxRateForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductTypeTaxRate_data = kwargs.get("ProductTypeTaxRate")
        try:
            form = cls.form(data=ProductTypeTaxRate_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.ProductTypeTaxRate_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductTypeTaxRateForm(Output):
    form = UpdateProductTypeTaxRateForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductTypeTaxRate_data = kwargs.get("ProductTypeTaxRate")
        try:
            form = cls.form(data=ProductTypeTaxRate.objects.get(
                id=ProductTypeTaxRate_data.pop("id")))
            if form.is_error:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields="")
                return cls(success=True, errors=Message.asdf_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class CreateProductVariantInventoryItemMixin(Output):
    form = CreateVariantInventoryItemForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductVariantInventoryItem_data = kwargs.get("ProductVariantInventoryItem")
        try:
            form = cls.form(data=ProductVariantInventoryItem_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.ProductVariantInventoryItem_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductVariantInventoryItemForm(Output):
    form = UpdateVariantInventoryItemForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductVariantInventoryItem_data = kwargs.get("ProductVariantInventoryItem")
        try:
            form = cls.form(data=ProductVariantInventoryItem.objects.get(
                id=ProductVariantInventoryItem_data.pop("id")))
            if form.is_error:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields="")
                return cls(success=True, errors=Message.asdf_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class CreateProductVariantMixin(Output):
    form = CreateProductVariantForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductVariant_data = kwargs.get("ProductVariant")
        try:
            form = cls.form(data=ProductVariant_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.ProductVariant_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class UpdateProductVariantForm(Output):
    form = UpdateProductVariantForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        ProductVariant_data = kwargs.get("ProductVariant")
        try:
            form = cls.form(data=ProductVariant.objects.get(
                id=ProductVariant_data.pop("id")))
            if form.is_error:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields="")
                return cls(success=True, errors=Message.asdf_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)
