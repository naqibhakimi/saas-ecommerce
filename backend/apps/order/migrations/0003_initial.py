# Generated by Django 4.1.5 on 2023-02-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("shipping", "0001_initial"),
        ("customer", "0003_initial"),
        ("invoice", "0002_initial"),
        ("discount", "0002_initial"),
        ("order", "0002_initial"),
        ("product", "0002_initial"),
        ("inventory", "0004_initial"),
        ("store", "0001_initial"),
        ("payment", "0001_initial"),
        ("giftcard", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="return",
            name="swap",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="store.swap",
            ),
        ),
        migrations.AddField(
            model_name="orderitemchange",
            name="line_item",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="invoice.lineitem",
            ),
        ),
        migrations.AddField(
            model_name="orderitemchange",
            name="order_edit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.orderedit",
            ),
        ),
        migrations.AddField(
            model_name="orderitemchange",
            name="original_line_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="invoice.lineitem",
            ),
        ),
        migrations.AddField(
            model_name="ordergiftcard",
            name="gift_card",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="giftcard.giftcard",
            ),
        ),
        migrations.AddField(
            model_name="ordergiftcard",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.order",
            ),
        ),
        migrations.AddField(
            model_name="orderedit",
            name="changes",
            field=models.ManyToManyField(related_name="+", to="order.orderitemchange"),
        ),
        migrations.AddField(
            model_name="orderedit",
            name="items",
            field=models.ManyToManyField(related_name="+", to="invoice.lineitem"),
        ),
        migrations.AddField(
            model_name="orderedit",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.order",
            ),
        ),
        migrations.AddField(
            model_name="orderedit",
            name="payment_collection",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="payment.paymentcollection",
            ),
        ),
        migrations.AddField(
            model_name="orderdiscount",
            name="discount",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="discount.discount",
            ),
        ),
        migrations.AddField(
            model_name="orderdiscount",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.order",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="billing_address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="customer.address",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="cart",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="store.cart",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="currency",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="payment.currency",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="customer.customer",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="discounts",
            field=models.ManyToManyField(
                related_name="+", through="order.OrderDiscount", to="discount.discount"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="draft_order",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.draftorder",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="gift_cards",
            field=models.ManyToManyField(
                related_name="+", through="order.OrderGiftCard", to="giftcard.giftcard"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="customer.region",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="sales_channel",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="store.saleschannel",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="shipping_address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="customer.address",
            ),
        ),
        migrations.AddField(
            model_name="draftorder",
            name="cart",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="store.cart",
            ),
        ),
        migrations.AddField(
            model_name="draftorder",
            name="order",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="order.order",
            ),
        ),
        migrations.AddField(
            model_name="claimorder",
            name="additional_items",
            field=models.ManyToManyField(related_name="+", to="invoice.lineitem"),
        ),
        migrations.AddField(
            model_name="claimorder",
            name="claim_items",
            field=models.ManyToManyField(related_name="+", to="order.claimitem"),
        ),
        migrations.AddField(
            model_name="claimorder",
            name="fulfillments",
            field=models.ManyToManyField(related_name="+", to="inventory.fulfillment"),
        ),
        migrations.AddField(
            model_name="claimorder",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.order",
            ),
        ),
        migrations.AddField(
            model_name="claimorder",
            name="return_order",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.return",
            ),
        ),
        migrations.AddField(
            model_name="claimorder",
            name="shipping_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="customer.address",
            ),
        ),
        migrations.AddField(
            model_name="claimorder",
            name="shipping_methods",
            field=models.ManyToManyField(
                related_name="+", to="shipping.shippingmethod"
            ),
        ),
        migrations.AddField(
            model_name="claimitem",
            name="claim_order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="order.claimorder",
            ),
        ),
        migrations.AddField(
            model_name="claimitem",
            name="images",
            field=models.ManyToManyField(to="order.claimimage"),
        ),
        migrations.AddField(
            model_name="claimitem",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="invoice.lineitem"
            ),
        ),
        migrations.AddField(
            model_name="claimitem",
            name="tags",
            field=models.ManyToManyField(related_name="+", to="order.claimtag"),
        ),
        migrations.AddField(
            model_name="claimitem",
            name="variant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="product.productvariant"
            ),
        ),
        migrations.AddField(
            model_name="claimimage",
            name="claim_item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="order.claimitem",
            ),
        ),
    ]
