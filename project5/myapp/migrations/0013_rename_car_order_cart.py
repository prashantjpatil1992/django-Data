# Generated by Django 4.2.5 on 2023-11-29 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='car',
            new_name='cart',
        ),
    ]
