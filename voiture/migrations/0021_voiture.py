# Generated by Django 4.1.6 on 2023-05-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0020_rename_photo_vehicule_vehicule_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='pht/%y')),
            ],
        ),
    ]
