# Generated by Django 4.1.7 on 2023-06-25 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses_processes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses_process',
            name='responsible_person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='houses_processes', to=settings.AUTH_USER_MODEL),
        ),
    ]
