from django.db import models
from django.utils.translation import ugettext_lazy as _
from Parking.enum import Vehicle_type, PriceType
from django.db.models import Q
# Create your models here.

class ParkingSlot(models.Model):
    ParkingSlotNo =models.CharField(max_length=15, primary_key=True)
    VehicleType = models.CharField(_('VehicleType'),choices=Vehicle_type.choices(), max_length=20)
    AvailableSlot= models.IntegerField()


class Ticket (models.Model):
    TicketNo = models.IntegerField()
    ParkingSlotNo = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    VehicleLicense = models.CharField(max_length=20)
    EntryTime= models.DateTimeField()
    ExitTime = models.DateTimeField(default=0)
    Amount = models.FloatField(default=0)



class Rate(models.Model):
    Duration= models.IntegerField()
    Price = models.FloatField()
    Price_Type = models.CharField(_('Price_Type'),choices=PriceType.choices(), max_length=20)
    Vehicle_Type = models.CharField(_('Vehicle_Type'),choices=Vehicle_type.choices(), max_length=20)




