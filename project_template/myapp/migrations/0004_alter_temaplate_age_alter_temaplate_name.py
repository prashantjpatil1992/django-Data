# Generated by Django 4.2.5 on 2023-10-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_second'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temaplate',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='temaplate',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]