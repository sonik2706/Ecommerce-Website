# Generated by Django 3.1.3 on 2021-02-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_customer_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Terms_and_conditions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(default='Kurier', max_length=6),
        ),
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('Przelewem', 'Przelewew'), ('Pobranie', 'Za Pobraniem')], default='d', max_length=9),
        ),
    ]
