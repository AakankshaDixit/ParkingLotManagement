# Generated by Django 3.2.8 on 2021-10-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0004_alter_rate_price_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='Price_Type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('Variable', 'Variable')], max_length=20, verbose_name='Price_Type'),
        ),
    ]