# Generated by Django 2.2 on 2019-08-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_patient_data_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_data',
            name='Mobile',
            field=models.IntegerField(default='0'),
        ),
    ]
