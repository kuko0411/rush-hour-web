# Generated by Django 2.1 on 2018-08-21 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0002_clear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clear',
            name='level',
        ),
        migrations.DeleteModel(
            name='Clear',
        ),
    ]
