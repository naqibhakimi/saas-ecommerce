# Generated by Django 4.1.5 on 2023-02-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('opt_out', models.BooleanField(default=False)),
                ('anonymize', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BatchJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('context', models.JSONField(blank=True, null=True)),
                ('result', models.JSONField(blank=True, null=True)),
                ('dry_run', models.BooleanField(blank=True, default=False)),
                ('pre_processed_at', models.DateTimeField(blank=True, null=True)),
                ('processing_at', models.DateTimeField(blank=True, null=True)),
                ('confirmed_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('canceled_at', models.DateTimeField(blank=True, null=True)),
                ('failed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fulfillment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('no_notification', models.BooleanField(null=True)),
                ('location_id', models.CharField(max_length=255, null=True)),
                ('tracking_numbers', models.JSONField(default=dict)),
                ('data', models.JSONField()),
                ('shipped_at', models.DateTimeField(null=True)),
                ('canceled_at', models.DateTimeField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('idempotency_key', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FulfillmentProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_installed', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('tracking_number', models.CharField(max_length=255)),
                ('idempotency_key', models.CharField(blank=True, max_length=255, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('fulfillment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='inventory.fulfillment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FulfillmentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('quantity', models.IntegerField()),
                ('fulfillment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.fulfillment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
