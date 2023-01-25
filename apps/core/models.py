from django.db import models
from uuid import uuid4
# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    
    class Meta:
        abstruct = True