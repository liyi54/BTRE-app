# Generated by Django 3.0.4 on 2020-03-24 21:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 21, 27, 23, 942870, tzinfo=utc)),
        ),
    ]
