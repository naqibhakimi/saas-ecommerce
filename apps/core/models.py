from django.db import models
from uuid import uuid4
# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        abstract = True