# Generated by Django 3.2.8 on 2022-09-07 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0039_alter_paiement_date_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 7, 11, 37, 11, 397465)),
        ),
    ]