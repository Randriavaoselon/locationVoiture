# Generated by Django 3.2.8 on 2022-07-31 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agence', '0006_alter_agence_useragence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agence',
            name='userAgence',
        ),
        migrations.AddField(
            model_name='agence',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loueurAgence', to=settings.AUTH_USER_MODEL),
        ),
    ]