from functools import total_ordering
from django.forms import ModelForm
from django.shortcuts import redirect, render
# import datetime
from django.urls import reverse
from .models import *
from .forms import *
from .utilities import helper_mytimedelta
from django.forms.models import model_to_dict
from django.db.models import Sum



def add_flight(request): 
    myFlight = FlightForm()
    if request.method == "POST":
        myFlight = FlightForm(request.POST)
        print(myFlight)
        if myFlight.is_valid():
            
            myFlight.save()        
            return redirect ("logo:logbook")
    context ={'myFlight':myFlight}
    return render(request, "logo/add_flight.html", context)

def update_flight(request,pk):
    flight = Flight.objects.get(id=pk)
    myFlight = FlightForm(instance=flight)
    
    if request.method =="POST":
        myFlight = FlightForm(request.POST, instance=flight)  
        if myFlight.is_valid():      
            myFlight.save()
            return redirect("logo:logbook")
    return render(request, "logo/add_flight.html", {'myFlight':myFlight})
    
def delete_flight(request,pk):
    flight = Flight.objects.get(id = pk)
    if request.method == "POST":
        flight.delete()
        return redirect('/')
    context = {'flight' : flight}
    return render(request, "logo/delete_flight.html", context)


def summary(request):
    # Total Hours calculation
    ttltimeobj = Flight.objects.aggregate(Sum('sectorTime'))
    ttltimeval = ttltimeobj['sectorTime__sum']
    total_hours = helper_mytimedelta(ttltimeval)

    # Total Night calculation
    ttlnighttimeobj = Flight.objects.aggregate(Sum('nightTime'))
    ttlnighttimeval = ttlnighttimeobj['nightTime__sum']
    total_night = helper_mytimedelta(ttlnighttimeval)

    context = {'total_hours':total_hours,'total_night': total_night}
    return render(request, "logo/summary.html",context)

def logbook(request):
    flights = Flight.objects.all()
    context = {'flights':flights}
    return render(request, "logo/logbook.html", context)


def flight_detail(request,pk):
    # method:1
    flight = FlightForm(data = model_to_dict(Flight.objects.get(id=pk)))
    # field_names = [f.name for f in Flight._meta.get_fields()]
    # print(field_names)
    #method:2
    # flight = get_object_or_404(Flight,id=pk)
    # class FlightView(ModelForm):
    #     class Meta:
    #         model=Flight
    #         fields=['flight_date','flightNum','tailNum',
    #             'pilot', 'depApt', 'arrApt',
    #             'depTime','arrTime','nightTime','pilotrole',
    #             'p1Time','p2Time','dayTime','sectorTime']

    # form = FlightView(instance = flight)

    return render(request,"logo/flight_detail.html", {
        'flight':flight
    })

def aircraft(request):
    aircrafts = Aircraft.objects.all()
    aircraftform = AircraftForm()

    if request.method =='POST':
        aircraftform = AircraftForm(request.POST)
        if aircraftform.is_valid():
            # aircraftform.clean()
            aircraftform.save()
            return redirect("logo:aircraft_list")
    context = {"aircrafts" : aircrafts, 'aircraftform' :aircraftform}
    return render(request, "logo/aircraft_list.html", context)

def delete_aircraft(request,pk):
    aircraft = Aircraft.objects.get(id = pk)
    if request.method == "POST":
        aircraft.delete()
        return redirect('logo:aircraft_list')
    context ={"aircraft":aircraft}
    return render(request,"logo/delete_aircraft.html", context)

def update_aircraft(request,pk):
    aircraftobj = Aircraft.objects.get(id=pk)
    aircrafts = Aircraft.objects.all()
    aircraftform = AircraftForm(instance=aircraftobj)
    if request.method == 'POST':
        aircraftform = AircraftForm(request.POST, instance = aircraftobj)
        if aircraftform.is_valid():
            aircraftform.save()
            return redirect("logo:aircraft_list")
    context = {"aircrafts":aircrafts, "aircraftform":aircraftform}
    return render(request, "logo/aircraft_list.html", context)

def people(request):
    people = People.objects.all()
    peopleform = PeopleForm()

    if request.method =="POST":
        peopleform = PeopleForm(request.POST)
        if peopleform.is_valid():
            peopleform.save()
        return redirect("logo:people")
    context = {"people":people, "peopleform":peopleform}
    return render(request, "logo/people.html",context)

def delete_person(request,pk):
    person = People.objects.get(id = pk)
    person.delete()
    return redirect("logo:people")

def airport(request):
    airports = Airport.objects.all()
    airportform = AirportForm()

    if request.method =="POST":
        airportform = AirportForm(request.POST)
        if airportform.is_valid():
            airportform.save()
        return redirect("logo:airport_list")
    context = {"airports":airports, "airportform":airportform}
    return render(request, "logo/airport_list.html",context)

def delete_airport(request,pk):
    airport = Airport.objects.get(id = pk)
    if request.method == "POST":
        airport.delete()
        return redirect('logo:airport_list')
    context ={"airport":airport}
    return render(request,"logo/delete_airport.html", context)

def update_airport(request,pk):
    placeobj = Airport.objects.get(id=pk)
    airports = Airport.objects.all()
    airportform = AirportForm(instance=placeobj)
    if request.method == 'POST':
        airportform = AirportForm(request.POST, instance = placeobj)
        if airportform.is_valid():
            airportform.save()
            return redirect("logo:airport_list")
    context = {"airports":airports, "airportform":airportform}
    return render(request, "logo/airport_list.html", context)