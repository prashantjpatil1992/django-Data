# Generated by Django 4.2.5 on 2023-12-13 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_address_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='product',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
    ]
