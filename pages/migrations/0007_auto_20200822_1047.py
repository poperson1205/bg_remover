# Generated by Django 3.1 on 2020-08-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200822_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefilemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
