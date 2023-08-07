# Generated by Django 4.1.7 on 2023-08-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0032_alter_notification_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="level",
            field=models.CharField(
                choices=[
                    ("info", "Info"),
                    ("warning", "Warning"),
                    ("danger", "Danger"),
                    ("success", "Success"),
                ],
                default="success",
                max_length=20,
            ),
        ),
    ]
