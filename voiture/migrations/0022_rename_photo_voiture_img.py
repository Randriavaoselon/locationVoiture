# Generated by Django 4.1.6 on 2023-05-02 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0021_voiture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voiture',
            old_name='photo',
            new_name='img',
        ),
    ]
