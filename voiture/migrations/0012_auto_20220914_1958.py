# Generated by Django 3.2.8 on 2022-09-14 16:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0011_remove_vehicule_prixkm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='id',
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='numImm',
            field=models.CharField(default=uuid.uuid4, max_length=10, primary_key=True, serialize=False),
        ),
    ]
