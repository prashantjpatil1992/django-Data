# Generated by Django 4.2.5 on 2023-10-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_django_khalid_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django_khalid',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
