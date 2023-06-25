# Generated by Django 4.1.7 on 2023-06-25 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family_residence_permit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('turkish_id', models.SmallIntegerField(default='1', verbose_name='Turkish ID number')),
                ('tc_id_expiry_date', models.DateField(default=datetime.date.today, verbose_name='TC expiry date')),
                ('passport_number', models.CharField(blank=True, max_length=20)),
                ('passport_expiry_date', models.DateField(default=datetime.date.today, verbose_name='Passport expiry date')),
                ('first_visit_date', models.DateField(default=datetime.date.today, verbose_name='First visit date to Turkiye')),
                ('family', models.CharField(blank=True, choices=[('spouse', 'Spouse'), ('child1', 'Child1'), ('child2', 'Child2'), ('child3', 'Child3'), ('child4', 'Child4')], max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('krstatus', models.CharField(choices=[('notapplied', '아직 신청하지 않음'), ('applicationneeded', '신청 필요'), ('announcedrequireddocuments', '필요서류 및 절차 공지 완료'), ('documentdeliverd', '서류 전달 완료'), ('translation', '서류 번역 완료'), ('notarization', '서류 공증 완료'), ('applied', '신청완료'), ('waitingforinterviewdate', '이민국 인터뷰 일자 공지 대기중'), ('announcedinterviewdate', '이민국 인터뷰 일자 공지 완료'), ('interviewcompleted', '이민국 인터뷰 완료'), ('revisitneeded', '다시 방문 필요'), ('revisitcompleted', '재방문 완료'), ('waitingforapproval', '승인 대기 중'), ('approvedandwaitforcard', '승인됨 카드 발급 대기 중'), ('carddeliveredphotoneeded', '카드 전달 완료됨, 총무팀에 거주증 사진 전송 필요'), ('postofficevisitneeded', '부재중으로 인해 우체국 방문 필요'), ('completed', '모든 절차 완료')], default='notapplied', max_length=150)),
                ('enstatus', models.CharField(choices=[('notapplied', 'Not applied'), ('applicationneeded', 'Application needed'), ('announcedrequireddocuments', 'Required documents and process were notified'), ('documentdeliverd', 'Document delivered'), ('translation', 'Translation completed'), ('notarization', 'Notarization completed'), ('applied', 'Applied'), ('waitingforinterviewdate', 'Waiting for interview date from immigration office'), ('announcedinterviewdate', 'immigration office announced interview date'), ('interviewcompleted', 'Interview completed'), ('revisitneeded', 'Revisit needed'), ('revisitcompleted', 'Revisit completed'), ('waitingforapproval', 'Waiting for approval'), ('approvedandwaitforcard', 'Approved and waiting for card'), ('carddeliveredphotoneeded', 'Card delivered, please send photos to GA team'), ('postofficevisitneeded', 'Please visit postoffice'), ('completed', 'Completed')], default='notapplied', max_length=150)),
                ('interview_place', models.CharField(default='', max_length=180)),
                ('interview_date', models.DateField(default=datetime.date.today, verbose_name='Interview date')),
                ('interview_time', models.TimeField(default='19:00', verbose_name='Interview time')),
                ('post_office', models.CharField(default='', max_length=180)),
            ],
            options={
                'verbose_name_plural': 'Family residence permits',
            },
        ),
    ]
