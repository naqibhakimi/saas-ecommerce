from apps.core.mutations import Output
from django.forms import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreateImageForm, CreatePriceListFrom, CreateProductCollectionForm, CreateProductFrom, CreateProductTagForm, UpdatePriceListForm, UpdateProductFrom, CreateProductTypeForm, UpdateProductTypeForm
from .constant import Message
from .models import PriceList, Product, ProductType


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
        print(product_data)
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

    @staticmethod
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


class CreateImageMixin(Output):
    form = CreateImageForm

    @staticmethod
    def resolve_mutation(cls, root, info, **kwargs):
        image_data = kwargs.get("")
        try:
            form = cls.form(data=image_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.IMAGE_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class CreateProductCollectionMixin(Output):
    form = CreateProductCollectionForm

    @staticmethod
    def resolve_mutation(cls, root, info, **kwargs):
        product_collection_data = kwargs.get("")
        try:
            form = cls.form(data=product_collection_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.sd)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)
