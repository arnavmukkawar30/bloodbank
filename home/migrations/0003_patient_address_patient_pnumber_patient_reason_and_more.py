# Generated by Django 4.0 on 2022-01-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_fname_patient_fname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='PNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='Reason',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Unit',
            field=models.IntegerField(default=0),
        ),
    ]
