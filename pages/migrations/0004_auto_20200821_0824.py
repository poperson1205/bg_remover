# Generated by Django 3.1 on 2020-08-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200821_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefilemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='input'),
        ),
    ]
