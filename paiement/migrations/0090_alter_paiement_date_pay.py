# Generated by Django 4.1.6 on 2023-04-30 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0089_alter_paiement_date_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 30, 11, 1, 27, 979822)),
        ),
    ]
