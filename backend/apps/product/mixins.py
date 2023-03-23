from apps.core.mutations import Output
from django.forms import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreatePriceListFrom, CreateProductFrom, UpdatePriceListForm, UpdateProductFrom
from .constant import Message
from .models import PriceList, Product


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
