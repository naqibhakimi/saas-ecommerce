from django.contrib import admin

# Register your models here.

from apps.core.models import BaseModel

for model in BaseModel.__subclasses__():
    admin.site.register(model)
