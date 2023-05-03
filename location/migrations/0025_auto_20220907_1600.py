# Generated by Django 3.2.8 on 2022-09-07 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0024_alter_location_loueur'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='dt_debut',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Date_debut'),
        ),
        migrations.AddField(
            model_name='location',
            name='dt_fin',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Date_fin'),
        ),
        migrations.AddField(
            model_name='location',
            name='dure',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
    ]