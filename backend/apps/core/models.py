import re

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="+")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="+")
    class Meta:
        abstract = True
