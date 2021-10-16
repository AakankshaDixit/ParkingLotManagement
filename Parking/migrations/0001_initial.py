# Generated by Django 3.2.8 on 2021-10-15 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('ParkingSlotNo', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('VehicleType', models.CharField(choices=[('Two Wheeler', 'Two Wheeler'), ('Four Wheeler', 'Four Wheeler')], max_length=20, verbose_name='VehicleType')),
                ('AvailableSlot', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duration', models.IntegerField()),
                ('Price', models.FloatField()),
                ('Price_Type', models.CharField(choices=[('PriceType.Fixed', 'Fixed'), ('PriceType.Variable', 'Variable')], max_length=20, verbose_name='Price_Type')),
                ('Vehicle_Type', models.CharField(choices=[('Two Wheeler', 'Two Wheeler'), ('Four Wheeler', 'Four Wheeler')], max_length=20, verbose_name='Vehicle_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketNo', models.IntegerField()),
                ('VehicleLicense', models.CharField(max_length=20)),
                ('EntryTime', models.DateTimeField()),
                ('ExitTime', models.DateTimeField()),
                ('Amount', models.FloatField()),
                ('ParkingSlotNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parking.parkingslot')),
            ],
        ),
    ]