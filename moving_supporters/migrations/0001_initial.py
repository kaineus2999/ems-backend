# Generated by Django 4.1.7 on 2023-06-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moving_supporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=180)),
                ('subtitle', models.CharField(default='', max_length=180)),
                ('contents', models.CharField(default='', max_length=180)),
                ('detailed_information', models.CharField(default='', max_length=180)),
                ('subtitle2', models.CharField(default='', max_length=180)),
                ('contents2', models.CharField(default='', max_length=180)),
                ('detailed_information2', models.CharField(default='', max_length=180)),
                ('subtitle3', models.CharField(default='', max_length=180)),
                ('contents3', models.CharField(default='', max_length=180)),
                ('detailed_information3', models.CharField(default='', max_length=180)),
                ('subtitle4', models.CharField(default='', max_length=180)),
                ('contents4', models.CharField(default='', max_length=180)),
                ('detailed_information4', models.CharField(default='', max_length=180)),
                ('subtitle5', models.CharField(default='', max_length=180)),
                ('contents5', models.CharField(default='', max_length=180)),
                ('detailed_information5', models.CharField(default='', max_length=180)),
                ('subtitle6', models.CharField(default='', max_length=180)),
                ('contents6', models.CharField(default='', max_length=180)),
                ('detailed_information6', models.CharField(default='', max_length=180)),
                ('subtitle7', models.CharField(default='', max_length=180)),
                ('contents7', models.CharField(default='', max_length=180)),
                ('detailed_information7', models.CharField(default='', max_length=180)),
                ('subtitle8', models.CharField(default='', max_length=180)),
                ('contents8', models.CharField(default='', max_length=180)),
                ('detailed_information8', models.CharField(default='', max_length=180)),
                ('subtitle9', models.CharField(default='', max_length=180)),
                ('contents9', models.CharField(default='', max_length=180)),
                ('detailed_information9', models.CharField(default='', max_length=180)),
                ('subtitle10', models.CharField(default='', max_length=180)),
                ('contents10', models.CharField(default='', max_length=180)),
                ('detailed_information10', models.CharField(default='', max_length=180)),
            ],
            options={
                'verbose_name_plural': 'Moving supporters',
            },
        ),
    ]