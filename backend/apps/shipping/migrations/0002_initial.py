# Generated by Django 4.1.5 on 2023-02-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("shipping", "0001_initial"),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customshippingoption",
            name="cart",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="store.cart"
            ),
        ),
        migrations.AddField(
            model_name="customshippingoption",
            name="shipping_option",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="shipping.shippingoption",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="shippingmethodtaxline",
            unique_together={("shipping_method", "code")},
        ),
        migrations.AlterUniqueTogether(
            name="customshippingoption",
            unique_together={("shipping_option", "cart")},
        ),
    ]
