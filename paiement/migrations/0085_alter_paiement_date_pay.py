# Generated by Django 4.1.6 on 2023-04-30 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0084_auto_20220928_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 30, 9, 52, 53, 995629)),
        ),
    ]
