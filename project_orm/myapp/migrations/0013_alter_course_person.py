# Generated by Django 4.2.5 on 2023-11-06 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_course_person_alter_course_cname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.person'),
        ),
    ]
