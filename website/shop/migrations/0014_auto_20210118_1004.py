# Generated by Django 3.1.3 on 2021-01-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20210116_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
