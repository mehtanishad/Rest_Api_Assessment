# Generated by Django 4.1.5 on 2023-07-25 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restApi_App", "0007_alter_item_created_at_alter_item_updated_at"),
    ]

    operations = [
        migrations.RenameModel(old_name="Item", new_name="Task",),
    ]