# Generated by Django 5.0.4 on 2024-04-29 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_parent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]