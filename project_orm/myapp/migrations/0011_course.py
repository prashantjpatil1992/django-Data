# Generated by Django 4.2.5 on 2023-11-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_id_remove_person_couser_delete_course_person_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
            ],
        ),
    ]
