# Generated by Django 4.1.7 on 2023-03-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green_cards_requests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available_country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Available countries',
            },
        ),
        migrations.AddField(
            model_name='green_cards_request',
            name='available_country',
            field=models.ManyToManyField(related_name='green_cards_requests', to='green_cards_requests.available_country'),
        ),
    ]
