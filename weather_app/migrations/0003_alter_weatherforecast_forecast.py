# Generated by Django 3.2.10 on 2021-12-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0002_weatherforecast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherforecast',
            name='forecast',
            field=models.JSONField(default={}),
        ),
    ]
