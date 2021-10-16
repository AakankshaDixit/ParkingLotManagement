from django.http import request
from django.shortcuts import redirect, render,HttpResponseRedirect
from Parking.enum import Vehicle_type,PriceType
import random
from datetime import datetime,date, timezone, tzinfo
import math
from django.db.models import Q
from django.contrib import messages

from Parking.models import ParkingSlot, Ticket, Rate

#from parking.serializers import ParkingSlotSerliazer, RateSerliazer, TicketSerliazer
# Create your views here.

def Index(request):
    
    return render(request,'index.html')

def UserInput(request):
    # TicketId=0
    # FirstSlot=0
    ShowTicket=''
    error=""
    
    if request.method=='POST':
        Vehicle_type=request.POST['VehicleType']
        VehicleLicense=request.POST['VehicleLicense']

        TicketId= random.randint(100,999)
        StrTicketID=str(TicketId)
        Entry_Time = datetime.now()
        try:
            FirstSlot =ParkingSlot.objects.filter(AvailableSlot=0,VehicleType=Vehicle_type).first()
             #print(FirstSlot)
            if(FirstSlot==None):
                    error="yes"

        except:
                error="no"

        if error!="yes":
        # ParkingSlot.objects.create(ParkingSlotNo=FirstSlot,VehicleType=Vehicle_type,AvailableSlot=1)
            FSlot= ParkingSlot.objects.filter(AvailableSlot=0,VehicleType=Vehicle_type).values("ParkingSlotNo")[0]
            #print(FSlot)
            F=FSlot['ParkingSlotNo']
            ParkingSlot.objects.filter(ParkingSlotNo=F).update(AvailableSlot=1)
            
            Ticket.objects.create(TicketNo=TicketId,ParkingSlotNo=FirstSlot,VehicleLicense=VehicleLicense,
            EntryTime= Entry_Time, ExitTime='2020-01-01 00:00:02.661')

    
        #----Render the ticketno and available slot
            ShowTicket = Ticket.objects.filter(TicketNo=TicketId,ParkingSlotNo_id=FirstSlot).values("TicketNo","ParkingSlotNo_id")
        

    d={'ST':ShowTicket, 'error':error}

    return render(request,'input.html',d)


def ExitParkingLot(request):
    error=""
    ErrorMessage=""
    if request.method=='POST':
        TicketNumber=request.POST['TicketNo']

    #updating exit time
        Exit_Time = datetime.now()
        try:
            t=Ticket.objects.filter(TicketNo=TicketNumber)
            print(t)
            if t.first()==None:
                error="yes"
        except:
            error="no"

        if error!="yes":
            Ticket.objects.filter(TicketNo=TicketNumber).update(ExitTime=Exit_Time)
                
            ExitAvailableSlot=Ticket.objects.filter(TicketNo=TicketNumber).values("EntryTime","ParkingSlotNo_id")
            print("exit",ExitAvailableSlot)
            SlotNo=ExitAvailableSlot[0]['ParkingSlotNo_id']
            TicketEntryTime=ExitAvailableSlot[0]['EntryTime']
            print("TicketEntry",TicketEntryTime)
            VType = ParkingSlot.objects.filter(ParkingSlotNo=SlotNo).values("VehicleType")[0]['VehicleType']
            
            #----------------
            TotalTime= Exit_Time.replace(tzinfo=None)-TicketEntryTime.replace(tzinfo=None)
            #print("TotalTime",TotalTime)

            Totalday=TotalTime.days
            #print("Totalday",Totalday)
            TotalHour=(TotalTime.seconds)/3600
            #print("TotalHour",TotalHour/3600)
            SumHours=Totalday*24+TotalHour
        
            #print("SumHours",SumHours)

            if SumHours>24:
                rate=Rate.objects.filter(Duration__lt=SumHours,Vehicle_Type=VType).order_by('-Duration').values("Price","Duration")[0]
                #print(rate)
                duration1=rate['Duration']
                #print("duration1",duration1)
                Price1=rate['Price']
                #print("price",Price1)

                out = Rate.objects.filter( Price=Price1).values("Price_Type")[0]['Price_Type']
                #print("out",out)
                if out=='Variable':
                    FinalAmount= math.ceil(SumHours/duration1)*Price1
                else:
                    pass

            else:
                rate=Rate.objects.filter(Duration__gt=SumHours,Vehicle_Type=VType).values("Price","Duration")[0]
                #print(rate)
                duration1=rate['Duration']
                #print("duration1",duration1)
                Price1=rate['Price']
                #print("price",Price1)
                FinalAmount=Price1

            print("FinalAmount",FinalAmount)

            Ticket.objects.filter(TicketNo=TicketNumber,ParkingSlotNo_id=SlotNo).update(Amount=FinalAmount)

            ParkingSlot.objects.filter(ParkingSlotNo=SlotNo).update(AvailableSlot=0)
            ErrorMessage="Slot is Exited"
            # return redirect('home')
            
        

    d={'e':ErrorMessage,'error':error} 

    return render(request,'ExitLot.html',d)


def ViewHistory(request):

    total=0
    gen=request.POST.get('LicenseNo')
    #print(gen)

    History = Ticket.objects.filter(ExitTime__gt='2020-01-01 00:00:02.661',VehicleLicense=gen).values("TicketNo","VehicleLicense","EntryTime","ExitTime","Amount","ParkingSlotNo_id")
 
    totalsum= Ticket.objects.filter(VehicleLicense=gen,ExitTime__gt='2020-01-01 00:00:02.661').values("Amount")
    #print(totalsum)
    for j in totalsum:
        total=total+j['Amount']
 
    #print(total)
 
    d={'H':History,'j':total}
    return render(request,'Viewhistory.html',d)

def ViewParkedVehicle(request):

    ASlot=ParkingSlot.objects.filter(AvailableSlot=1).values("ParkingSlotNo")
    #print(ASlot)

    

    ParkedVehicle = Ticket.objects.filter(ParkingSlotNo__in=[value['ParkingSlotNo'] for value in ASlot]).values("TicketNo","VehicleLicense","ParkingSlotNo_id")

    d ={'PV':ParkedVehicle}

    return render(request,'ParkedVehicle.html',d)

 
    


