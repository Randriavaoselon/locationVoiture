# Generated by Django 3.2.8 on 2022-07-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_agence', models.CharField(max_length=100, null=True)),
                ('adresse_agence', models.CharField(max_length=100, null=True)),
                ('tel_agence', models.PositiveIntegerField()),
                ('email_agence', models.EmailField(max_length=254)),
                ('fax_agence', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'agence',
            },
        ),
    ]
