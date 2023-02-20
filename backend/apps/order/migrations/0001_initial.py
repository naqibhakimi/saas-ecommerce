# Generated by Django 4.1.5 on 2023-02-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('url', models.CharField(max_length=255)),
                ('metadata', models.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClaimItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('reason', models.CharField(choices=[('missing_item', 'Missing Item'), ('wrong_item', 'Wrong Item'), ('production_failure', 'Production Failure'), ('other', 'Other')], max_length=255)),
                ('note', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('metadata', models.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClaimOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('payment_status', models.CharField(choices=[('na', 'NA'), ('not_refunded', 'NOT_REFUNDED'), ('refunded', 'REFUNDED')], default='na', max_length=20)),
                ('fulfillment_status', models.CharField(choices=[('na', 'NA'), ('not_refunded', 'NOT_REFUNDED'), ('refunded', 'REFUNDED')], default='not_fulfilled', max_length=20)),
                ('type', models.CharField(choices=[('refund', 'REFUND'), ('replace', 'REPLACE')], max_length=20)),
                ('refund_amount', models.IntegerField(blank=True, null=True)),
                ('canceled_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('no_notification', models.BooleanField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('idempotency_key', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClaimTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.CharField(max_length=255, unique=True)),
                ('metadata', models.JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DraftOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('completed', 'COMPLETED')], default='OPEN', max_length=10)),
                ('canceled_at', models.DateTimeField(null=True)),
                ('completed_at', models.DateTimeField(null=True)),
                ('no_notification_order', models.BooleanField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('idempotency_key', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('completed', 'COMPLETED'), ('archived', 'ARCHIVED'), ('canceled', 'CANCELED'), ('requires_action', 'REQUIRES_ACTION')], default='Not PAID', max_length=20)),
                ('fulfillment_status', models.CharField(choices=[('not_fulfilled', 'NOT_FULFILLED'), ('partially_fulfilled', 'PARTIALLY_FULFILLED'), ('fulfilled', 'FULFILLED'), ('partially_shipped', 'PARTIALLY_SHIPPED'), ('shipped', 'SHIPPED'), ('partially_returned', 'PARTIALLY_RETURNED'), ('returned', 'RETURNED'), ('canceled', 'CANCELED'), ('requires_action', 'REQUIRES_ACTION')], default='NOT_FULFILLED', max_length=20)),
                ('payment_status', models.CharField(choices=[('not_paid', 'NOT PAID'), ('awaiting', 'AWAITING'), ('captured', 'CAPTURED'), ('partially_refunded', 'PARTIALLY REFUNDED'), ('refunded', 'REFUNDED'), ('canceled', 'CANCELED'), ('requires_action', 'REQUIRES ACTION')], default='NOT PAID', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('order_number', models.CharField(max_length=255, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('subtotal_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tax_rate', models.FloatField(null=True)),
                ('canceled_at', models.DateField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('no_notification', models.BooleanField(null=True)),
                ('idempotency_key', models.CharField(max_length=255, null=True)),
                ('external_id', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_total', models.IntegerField()),
                ('discount_total', models.FloatField()),
                ('tax_total', models.FloatField(null=True)),
                ('refunded_total', models.FloatField()),
                ('total', models.FloatField()),
                ('sub_total', models.FloatField()),
                ('paid_total', models.FloatField()),
                ('refundable_amount', models.FloatField()),
                ('gift_card_total', models.FloatField()),
                ('gift_card_tax_total', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderEdit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('internal_note', models.TextField(null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('requested_by', models.CharField(max_length=255, null=True)),
                ('requested_at', models.DateTimeField(null=True)),
                ('confirmed_by', models.CharField(max_length=255, null=True)),
                ('confirmed_at', models.DateTimeField(null=True)),
                ('declined_by', models.CharField(max_length=255, null=True)),
                ('declined_reason', models.TextField(null=True)),
                ('declined_at', models.DateTimeField(null=True)),
                ('canceled_by', models.CharField(max_length=255, null=True)),
                ('canceled_at', models.DateTimeField(null=True)),
                ('shipping_total', models.IntegerField()),
                ('discount_total', models.FloatField()),
                ('tax_total', models.FloatField(null=True)),
                ('total', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('gift_card_total', models.FloatField()),
                ('gift_card_tax_total', models.FloatField()),
                ('difference_due', models.FloatField()),
                ('status', models.CharField(choices=[('confirmed', 'CONFIRMED'), ('declined', 'DECLINED'), ('requested', 'REQUESTED'), ('created', 'CREATED'), ('canceled', 'CANCELED')], default='CREATED', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderGiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItemChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('type', models.CharField(choices=[('item_add', 'ITEM_ADD'), ('item_remove', 'ITEM_REMOVE'), ('item_update', 'ITEM_UPDATE')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('requested', 'REQUESTED'), ('received', 'RECEIVED'), ('requires_action', 'REQUIRES_ACTION'), ('canceled', 'CANCELED')], default='REQUESTED', max_length=20)),
                ('shipping_data', models.JSONField(null=True)),
                ('refund_amount', models.FloatField()),
                ('received_at', models.DateTimeField(null=True)),
                ('no_notification', models.BooleanField()),
                ('metadata', models.JSONField(null=True)),
                ('idempotency_key', models.CharField(max_length=100, null=True)),
                ('claim_order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='order.claimorder')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='order.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReturnReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.CharField(max_length=255, unique=True)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('parent_return_reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.returnreason')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReturnItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('quantity', models.IntegerField()),
                ('is_requested', models.BooleanField(default=True)),
                ('requested_quantity', models.IntegerField(null=True)),
                ('received_quantity', models.IntegerField(null=True)),
                ('note', models.TextField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='return_items', to='invoice.lineitem')),
                ('reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='order.returnreason')),
                ('return_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='return_items', to='order.return')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]