# Generated by Django 4.2.4 on 2023-08-21 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
    ]