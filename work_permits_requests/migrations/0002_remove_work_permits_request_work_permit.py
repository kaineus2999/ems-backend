# Generated by Django 4.1.7 on 2023-03-11 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_permits_requests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work_permits_request',
            name='work_permit',
        ),
    ]