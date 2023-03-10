# Generated by Django 4.1.5 on 2023-02-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("order", "0002_initial"),
        ("invoice", "0001_initial"),
        ("product", "0002_initial"),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lineitem",
            name="cart",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="store.cart",
            ),
        ),
        migrations.AddField(
            model_name="lineitem",
            name="claim_order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="order.claimorder",
            ),
        ),
        migrations.AddField(
            model_name="lineitem",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="order.order",
            ),
        ),
        migrations.AddField(
            model_name="lineitem",
            name="order_edit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="order.orderedit",
            ),
        ),
        migrations.AddField(
            model_name="lineitem",
            name="original_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="invoice.lineitem",
            ),
        ),
        migrations.AddField(
            model_name="lineitem",
            name="swap",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="store.swap",
            ),
        ),
        migrations.AddField(
            model_name="lineitem",
            name="variant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="product.productvariant",
            ),
        ),
    ]
