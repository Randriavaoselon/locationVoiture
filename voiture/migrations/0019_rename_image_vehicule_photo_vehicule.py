# Generated by Django 4.1.6 on 2023-04-30 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0018_rename_images_vehicule_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicule',
            old_name='image',
            new_name='photo_vehicule',
        ),
    ]
