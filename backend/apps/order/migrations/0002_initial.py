# Generated by Django 4.1.5 on 2023-02-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("shipping", "0001_initial"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="return",
            name="shipping_method",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="shipping.shippingmethod",
            ),
        ),
    ]
