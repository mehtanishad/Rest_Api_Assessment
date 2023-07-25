# Generated by Django 4.1.4 on 2023-03-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restApi_App", "0004_item_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="content",
            field=models.TextField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="locationName",
            field=models.TextField(max_length=100, unique=True),
        ),
    ]