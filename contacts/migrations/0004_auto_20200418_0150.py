# Generated by Django 3.0.4 on 2020-04-18 00:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20200417_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='inquiry_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 0, 50, 52, 809864, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
