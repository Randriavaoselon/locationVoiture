# Generated by Django 3.2.8 on 2022-09-11 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0032_auto_20220911_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='dt_debut',
        ),
        migrations.RemoveField(
            model_name='location',
            name='dt_fin',
        ),
        migrations.RemoveField(
            model_name='location',
            name='dure',
        ),
    ]
