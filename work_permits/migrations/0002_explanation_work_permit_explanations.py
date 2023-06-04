# Generated by Django 4.1.7 on 2023-06-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_permits', '0001_initial'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='work_permit',
            name='explanations',
            field=models.ManyToManyField(related_name='work_permits', to='work_permits.explanation'),
        ),
    ]
