# Generated by Django 4.1.4 on 2023-03-22 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("restApi_App", "0003_rename_date_added_item_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="updated_at",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
