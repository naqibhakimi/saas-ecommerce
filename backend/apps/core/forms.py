from django import forms
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
from django.db.models.query_utils import DeferredAttribute
from graphql_relay import from_global_id


def is_foreignkey(field):
    return isinstance(field, ForwardManyToOneDescriptor)

def is_primarykey(field, key):
    return isinstance(field, DeferredAttribute) and key == 'id'

def get_fields(form, data):
    for key, value in vars(form._meta.model).items():
        if (is_foreignkey(value) or is_primarykey(value, key)) and data.get(key) :
            yield (key, int(from_global_id(data.get(key)).id))


class BaseForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     data = kwargs.get("data", {})
    #     data.update(get_fields(self, data))
    #     print(args, kwargs)

    #     if not data:
    #         super().__init__(*args, **kwargs)

    #     if data.get('id') and not data:
    #         instace = self._meta.model.objects.get(id=data.get('id'))
    #         super().__init__(data=data, instace=instace,  *args, **kwargs)
    #     else:
    #         super().__init__(data=data, *args, **kwargs)

    class Meta:
        abstruct = True
