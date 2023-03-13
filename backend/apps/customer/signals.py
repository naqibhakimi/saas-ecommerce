
from django.db.models.signals import post_save
from .models import Customer, Address


def post_save_customer(instance, created, *args, **kwargs):
    # print(instance, created, args, kwargs)
    if created:
        instance.billing_address = Address.objects.create()
        instance.save()


post_save.connect(post_save_customer, sender=Customer)