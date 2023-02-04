# Generated by Django 4.1.5 on 2023-02-04 18:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('thumbnail', models.TextField(null=True)),
                ('is_return', models.BooleanField(default=False)),
                ('is_giftcard', models.BooleanField(default=False)),
                ('should_merge', models.BooleanField(default=True)),
                ('allow_discounts', models.BooleanField(default=True)),
                ('has_shipping', models.BooleanField(null=True)),
                ('unit_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('fulfilled_quantity', models.PositiveIntegerField(null=True)),
                ('returned_quantity', models.PositiveIntegerField(null=True)),
                ('shipped_quantity', models.PositiveIntegerField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('includes_tax', models.BooleanField(default=False)),
                ('refundable', models.PositiveIntegerField(null=True)),
                ('subtotal', models.PositiveIntegerField(null=True)),
                ('tax_total', models.PositiveIntegerField(null=True)),
                ('total', models.PositiveIntegerField(null=True)),
                ('original_total', models.PositiveIntegerField(null=True)),
                ('original_tax_total', models.PositiveIntegerField(null=True)),
                ('discount_total', models.PositiveIntegerField(null=True)),
                ('gift_cart_total', models.PositiveIntegerField(null=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='store.cart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LineItemTaxLine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.lineitem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LineItemAdjustment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discount.discount')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='invoice.lineitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
