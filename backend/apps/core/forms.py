from django import forms
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
from graphql_relay import from_global_id


def is_foreignkey(field):
    return isinstance(field, ForwardManyToOneDescriptor)


def get_fields(form, data):
    for key, value in vars(form._meta.model).items():
        if is_foreignkey(value) and data.get(key):
            yield (key, from_global_id(data.get(key)).id)


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        data = kwargs.get("data", {})
        data.update(get_fields(self, data))
        super().__init__(*args, **kwargs)

    class Meta:
        abstruct = True
