# Generated by Django 4.0 on 2022-01-19 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_patient_address_patient_pnumber_patient_reason_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
