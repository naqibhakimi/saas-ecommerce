# Generated by Django 4.1.7 on 2023-03-11 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_address_first_name_remove_address_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='region',
            name='countries',
        ),
        migrations.RemoveField(
            model_name='region',
            name='fulfillment_providers',
        ),
        migrations.RemoveField(
            model_name='region',
            name='payment_providers',
        ),
    ]
