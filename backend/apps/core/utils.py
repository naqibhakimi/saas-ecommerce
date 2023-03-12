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
           data[key] =  int(from_global_id(data.get(key)).id)
    if data.get('id') is not None:
         return {'data': data, 'instance': form._meta.model.objects.get(id=data.get('id'))}
    return {'data': data}
