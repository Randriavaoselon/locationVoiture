# Generated by Django 3.2.8 on 2022-07-18 13:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0009_auto_20220718_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_compte', models.PositiveIntegerField(default=0)),
                ('montants', models.PositiveIntegerField(default=0)),
                ('date_pay', models.DateField(default=datetime.date.today, verbose_name='Date paiement')),
                ('nom_client', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]