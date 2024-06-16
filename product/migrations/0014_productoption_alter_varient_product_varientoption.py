# Generated by Django 5.0.4 on 2024-05-04 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_varient_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Option title')),
            ],
        ),
        migrations.AlterField(
            model_name='varient',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product'),
        ),
        migrations.CreateModel(
            name='VarientOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250, verbose_name='Varient option value')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.productoption', verbose_name='option')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
            ],
        ),
    ]
