# Generated by Django 3.1.3 on 2021-02-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_auto_20210214_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
