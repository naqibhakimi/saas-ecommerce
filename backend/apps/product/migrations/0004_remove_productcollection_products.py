# Generated by Django 4.1.7 on 2023-03-21 19:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productcollection",
            name="products",
        ),
    ]