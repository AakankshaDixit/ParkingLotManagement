# Generated by Django 3.2.8 on 2021-10-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0002_auto_20211015_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ExitTime',
            field=models.DateTimeField(default=0),
        ),
    ]