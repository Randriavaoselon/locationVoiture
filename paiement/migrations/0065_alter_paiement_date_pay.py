# Generated by Django 3.2.8 on 2022-09-09 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0064_alter_paiement_date_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 9, 22, 35, 49, 35978)),
        ),
    ]
