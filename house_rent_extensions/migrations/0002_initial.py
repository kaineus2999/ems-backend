# Generated by Django 4.1.7 on 2023-06-25 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('house_rent_extensions', '0001_initial'),
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house_rent_extension',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_rent_extensions', to='houses.house'),
        ),
    ]
