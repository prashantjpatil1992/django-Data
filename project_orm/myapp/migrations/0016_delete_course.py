# Generated by Django 4.2.5 on 2023-11-06 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_course_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]