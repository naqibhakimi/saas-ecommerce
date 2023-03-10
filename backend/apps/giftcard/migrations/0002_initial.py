# Generated by Django 4.1.5 on 2023-02-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("giftcard", "0001_initial"),
        ("customer", "0001_initial"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="giftcardtransaction",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.order",
            ),
        ),
        migrations.AddField(
            model_name="giftcard",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="customer.region"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="giftcardtransaction",
            unique_together={("gift_card_id", "order_id")},
        ),
    ]
