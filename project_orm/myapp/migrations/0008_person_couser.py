# Generated by Django 4.2.5 on 2023-11-06 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_course_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Couser',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
        ),
    ]