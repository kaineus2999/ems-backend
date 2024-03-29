# Generated by Django 4.1.7 on 2023-06-26 17:38

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('family_residence_permits_preparation_documents', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_birth_date2',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Child birth date'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_birth_date3',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Child birth date'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_birth_date4',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Child birth date'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_address2',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_address3',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_address4',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_authorized_person2',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_authorized_person3',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_authorized_person4',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_cellphone_number2',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_cellphone_number3',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_cellphone_number4',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_consulate_date2',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of Consulate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_consulate_date3',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of Consulate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_consulate_date4',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of Consulate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_date2',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of child family relations certificate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_date3',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of child family relations certificate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_date4',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of child family relations certificate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_number2',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_number3',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_number4',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_public_office2',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_public_office3',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_public_office4',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_time2',
            field=models.TimeField(blank=True, default='19:00', verbose_name='Document time of child family relations certificate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_time3',
            field=models.TimeField(blank=True, default='19:00', verbose_name='Document time of child family relations certificate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_time4',
            field=models.TimeField(blank=True, default='19:00', verbose_name='Document time of child family relations certificate'),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_person_who_request2',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_person_who_request3',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_person_who_request4',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_responsible_person2',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_responsible_person3',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_responsible_person4',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_gender2',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_gender3',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_gender4',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_id2',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_id3',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_id4',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_name2',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_name3',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AddField(
            model_name='family_residence_permits_preparation_document',
            name='child_name4',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_birth_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Child birth date'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_address',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_authorized_person',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_cellphone_number',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_consulate_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of Consulate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of child family relations certificate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_number',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_public_office',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_document_time',
            field=models.TimeField(blank=True, default='19:00', verbose_name='Document time of child family relations certificate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_person_who_request',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_family_relations_certificate_responsible_person',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_gender',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_id',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='child_name',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='criminal_record_address',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='criminal_record_document_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of Criminal record certificate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='criminal_record_document_date_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Document time of Criminal record certificate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='criminal_record_document_number',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='criminal_record_person_who_request',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_address',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_approved_date',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_approved_person',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_approved_place',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_authorized_person',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_cellphone_number',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_document_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document date of Marriage certificate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_document_number',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_document_public_office',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_document_time',
            field=models.TimeField(blank=True, default='19:00', verbose_name='Document time of Marriage certificate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_marriage_date',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_person_who_request',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='marriage_certificate_responsible_person',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='national_police_service_address',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='national_police_service_authorized_official',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='national_police_service_consulate_result',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='consulate result date of National police service certificate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='national_police_service_document_number',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='national_police_service_document_result',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Document result date of National police service certificate'),
        ),
        migrations.AlterField(
            model_name='family_residence_permits_preparation_document',
            name='national_police_service_official',
            field=models.CharField(blank=True, default='', max_length=180),
        ),
    ]
