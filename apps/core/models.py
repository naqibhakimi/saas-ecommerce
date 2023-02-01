from django.db import models
from uuid import uuid4
import re 
# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        abstract = True


def collect_class():
    for sub in BaseModel.__subclasses__():
        print(f"""class {sub.__name__}Query:
        {re.sub(r'(?<!^)(?=[A-Z])', '_', sub.__name__).lower()}s = DjangoConnectionField({sub.__name__}Node)
        {re.sub(r'(?<!^)(?=[A-Z])', '_', sub.__name__).lower()} = graphene.Field({sub.__name__}Node, id=graphene.ID())
        """)
        


