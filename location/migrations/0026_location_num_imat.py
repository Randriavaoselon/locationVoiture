# Generated by Django 3.2.8 on 2022-09-08 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0011_remove_vehicule_prixkm'),
        ('location', '0025_auto_20220907_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='num_Imat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='num_Imat', to='voiture.vehicule'),
        ),
    ]
