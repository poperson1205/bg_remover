# Generated by Django 3.1 on 2020-08-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfilemodel',
            name='title',
        ),
        migrations.AddField(
            model_name='uploadfilemodel',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
