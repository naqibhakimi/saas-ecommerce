# Generated by Django 4.1.7 on 2023-03-22 22:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0009_alter_address_metadata_alter_region_currency_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="metadata",
            field=models.JSONField(blank=True, null=True, verbose_name=dict),
        ),
    ]
