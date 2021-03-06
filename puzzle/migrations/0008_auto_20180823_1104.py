# Generated by Django 2.1 on 2018-08-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0007_auto_20180823_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='square_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='level',
            name='square_width',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='level',
            name='height',
            field=models.IntegerField(default=310),
        ),
        migrations.AlterField(
            model_name='level',
            name='width',
            field=models.IntegerField(default=310),
        ),
    ]
