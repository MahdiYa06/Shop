# Generated by Django 5.0.4 on 2024-05-07 14:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_shoppingcard_is_primary'),
        ('product', '0015_remove_varientoption_product_varientoption_varient'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Created', 'Order Created'), ('Cancled', 'Order Cancled'), ('Finished', 'Order Paid'), ('Proccessed', 'Order Proccessed'), ('Sent', 'Order Sent To The Delivery System'), ('Delivered', 'Order Delivered To Customer')], max_length=50, verbose_name='Order Status')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Varient title')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Varient price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Order')),
                ('varient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.varient', verbose_name='Varient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
