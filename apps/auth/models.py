from django.db import models
from apps.core.models import BaseModel
class Oauth(BaseModel):
    display_name = models.CharField(max_length=255)
    application_name = models.CharField(max_length=255, unique=True)
    install_url = models.CharField(max_length=255, null=True)
    uninstall_url = models.CharField(max_length=255, null=True)
    data = models.JSONField(null=True)


class PublishableApiKeySalesChannel(BaseModel):
    sales_channel_id = models.CharField(max_length=100, unique=True)
    publishable_key_id = models.CharField(max_length=100, unique=True)

class PublishableApiKey(BaseModel):
    created_by = models.CharField(max_length=100, null=True)
    revoked_by = models.CharField(max_length=100, null=True)
    revoked_at = models.DateTimeField(null=True)
    title = models.CharField(max_length=100)

