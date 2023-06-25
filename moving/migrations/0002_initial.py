# Generated by Django 4.1.7 on 2023-06-25 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('moving', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='moving',
            name='responsible_person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='moving', to=settings.AUTH_USER_MODEL),
        ),
    ]
