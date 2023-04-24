# Generated by Django 4.1.7 on 2023-04-21 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=180)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('detailed_information', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('detailed_information', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Explanations',
            },
        ),
        migrations.CreateModel(
            name='Company_cars_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('accident_location', models.CharField(blank=True, choices=[('istanbul', 'Istanbul'), ('izmit', 'Izmit')], max_length=10)),
                ('accident_type', models.CharField(blank=True, choices=[('car_crush', 'Car crush'), ('towed_car', 'Towed car'), ('flat_tire', 'Flat tire')], max_length=10)),
                ('documents', models.ManyToManyField(related_name='company_cars_requests', to='company_cars_requests.document')),
                ('expat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_cars_requests', to=settings.AUTH_USER_MODEL)),
                ('explanations', models.ManyToManyField(related_name='company_cars_requests', to='company_cars_requests.explanation')),
            ],
            options={
                'verbose_name_plural': 'Company cars requests',
            },
        ),
    ]
