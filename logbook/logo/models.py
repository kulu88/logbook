

from django.db import models
from django.urls import reverse
import datetime


# from .utilities import timedelta_to_datetime
# from django.utils.duration import _get_duration_components
# from django.forms.fields import DurationField

# Create your models here.

# class Hour(models.Model):
#     sectorHour = models.DurationField(blank = False, default=datetime.timedelta(seconds=0))
#     p1Hour = models.DurationField(blank = True, default=datetime.timedelta(seconds=0))
#     p2Hour = models.DurationField(blank = True, default=datetime.timedelta(seconds=0))
#     dayHour = models.DurationField(blank = True, default=datetime.timedelta(seconds=0))
#     nightHour = models.DurationField(blank = True, default=datetime.timedelta(seconds=0))
    # totalHour = models.DurationField()

'''
def duration_string(duration):
    days = duration.days
    seconds = duration.seconds
    microseconds = duration.microseconds

    minutes = seconds // 60
    seconds = seconds % 60

    hours = minutes // 60
    minutes = minutes % 60

    string = '{:02d}:{:02d}'.format(hours, minutes)
    # if days:
    #     string = '{} '.format(days) + string
    # if microseconds:
    #     string += '.{:06d}'.format(microseconds)
    return string


class MyDurationField(DurationField):

    def prepare_value(self, value):
        if isinstance(value, datetime.timedelta):
            return duration_string(value)
        return value

'''
        


class Aircraft(models.Model):
    tailNumber = models.CharField(verbose_name="Registration Number",max_length=20, blank=True,unique=True, null=True)
    type = models.CharField(verbose_name="Aircraft Type",max_length=50, blank=True, null=True)
    # sectorTime = models.ForeignKey(Hour,blank = False,on_delete=models.CASCADE)

    class Meta:
        ordering = ['tailNumber']

    def __str__(self):
        return f"{self.tailNumber} ({self.type})"


class People(models.Model):
    name = models.CharField(verbose_name="Pilot's Name",max_length= 50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name


class Airport(models.Model):
    aptIcao = models.CharField(verbose_name="ICAO Code",max_length=4, blank = True,unique=True )
    aptIata = models.CharField(verbose_name="IATA Code",max_length=3, blank = True,unique=True)
    aptCity = models.CharField(verbose_name="City's Name",max_length=20, blank = True)

    def __str__(self):
        # TODO remove try except
        try:
            return self.aptIcao 
        except:
            pass

    # def get_absolute_url(self):
    #     return reverse("update_airport", kwargs={"pk": self.pk})
    


class Flight(models.Model):
    CHOICE = [
        # ('---','---'),
        ('P1','Pilot in Command'),
        ('P2','First Officer')
    ]
    flightDate = models.DateField(verbose_name="Date of the Flight (DdMmYy) ")
    flightNum = models.CharField(verbose_name="Flight Number",max_length=10, blank=True)
    tailNum = models.ForeignKey(Aircraft, verbose_name="Select Aircraft",blank=True, on_delete=models.PROTECT, null=True)
    coPilot = models.ForeignKey(People,verbose_name="Select First Officer", blank=True ,on_delete=models.PROTECT, null=True)
    depApt = models.ForeignKey(Airport, related_name = "departure", verbose_name="Select Departure Airport",blank=True, on_delete=models.PROTECT, null=True)
    arrApt = models.ForeignKey(Airport, related_name = "arrival",verbose_name="Select Arrival Airport", blank=True, on_delete=models.PROTECT, null=True)
    depTime = models.TimeField(verbose_name="Departure Time (HhMm) ",blank=True,null=True)
    arrTime = models.TimeField(verbose_name="Arrival Time (HhMm) ",blank=True,null=True)
    pilotRole = models.CharField(verbose_name="Select Pilot Role",blank=True, max_length=2, choices=CHOICE, null=True)
    nightTime = models.DurationField(verbose_name="Night",blank = True, default=datetime.timedelta(seconds=0),null=True)
    dayTime = models.DurationField(verbose_name="Day",blank = True, default=datetime.timedelta(seconds=0),null=True)
    sectorTime = models.DurationField(verbose_name="Block",blank = True, default=datetime.timedelta(seconds=0),null=True)
    p1Time = models.DurationField(verbose_name="PIC",blank = True, default=datetime.timedelta(seconds=0),null=True)
    p2Time = models.DurationField(verbose_name="P2",blank = True, default=datetime.timedelta(seconds=0),null=True)

    class Meta:
        ordering = ['-flightDate','-depTime']
    
    def __str__(self):
        return f"{self.flightDate} : {self.depApt}  ->  {self.arrApt}"

    def get_absolute_url(self):
        return reverse('logo:update_flight', kwargs={"pk": self.pk})
    
    def timedelta_to_datetime(self,timedelta):
        try:
            date = self.flightDate
            ttlseconds = timedelta.total_seconds()
            hours = int(ttlseconds//3600)
            minutes = int((ttlseconds%3600)//60)
            time = datetime.time(hours, minutes)
            return datetime.datetime.combine(date,time)
        except:
            pass

    @property
    def get_flight_duration(self):
        fltdate = self.flightDate
        fltdeptime = self.depTime
        fltarrtime = self.arrTime
        try:
            sectortime = (datetime.datetime.combine(fltdate,fltarrtime)-datetime.datetime.combine(fltdate,fltdeptime))
            zerotimedelta = datetime.timedelta(seconds=0)
            oneDay = datetime.timedelta(hours=24)
            if sectortime < zerotimedelta:
                sectortime = oneDay + sectortime
            return sectortime
        except:
            pass

    @property
    def calculate_day_time(self):
        try:
            flightduration = self.sectorTime
            nightduration = self.nightTime
            durationdatetime = self.timedelta_to_datetime( flightduration)
            nightdatetime = self.timedelta_to_datetime(nightduration)
            daytime = durationdatetime - nightdatetime
            return daytime
        except:
            pass
        
    def save(self, *args, **kwargs):
        # if self.id:
            # myflight = FlightForm(id=pk)
        self.sectorTime = self.get_flight_duration
        self.dayTime = self.calculate_day_time
        if self.pilotRole =="P1":
            self.p1Time = self.sectorTime
        elif self.pilotRole == "P2":
            self.p2Time = self.sectorTime
        super(Flight, self).save(*args,**kwargs)

