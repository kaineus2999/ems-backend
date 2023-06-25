# Generated by Django 4.1.7 on 2023-06-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moving_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('responsible_person_name', models.CharField(default='', max_length=180)),
                ('cellphone_number', models.PositiveSmallIntegerField(default='1', verbose_name='Cellphone number')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('explain', models.CharField(default='', max_length=500)),
                ('detailed_information', models.CharField(default='', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Moving companies',
            },
        ),
    ]
