# Generated by Django 3.1.3 on 2021-01-16 15:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210115_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 16, 15, 12, 30, 126746, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default="To be, or not to be: that is the question: whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a"),
        ),
    ]
