# Generated by Django 3.2.8 on 2022-09-14 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0072_auto_20220913_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 14, 19, 8, 24, 606987)),
        ),
    ]
