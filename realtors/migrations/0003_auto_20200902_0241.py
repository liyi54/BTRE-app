# Generated by Django 3.0.4 on 2020-09-02 01:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20200324_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 2, 1, 41, 48, 75838, tzinfo=utc)),
        ),
    ]
