# Generated by Django 5.0.4 on 2024-05-09 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_shopping_is_primary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shopping',
            new_name='Shipping',
        ),
    ]