from django.forms import ModelForm

from .widgets import DateSelectorWidget, TimeSelectorWidget
from .models import *


class AircraftForm(ModelForm):
    class Meta:
        model = Aircraft
        fields = '__all__'


class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = '__all__'


class AirportForm(ModelForm):
    class Meta:
        model = Airport
        fields = "__all__"


class FlightForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance or instance.pk:
            self.fields['nightTime'].widget.attrs['readonly'] = True
            self.fields['dayTime'].widget.attrs['readonly'] = True
            self.fields['sectorTime'].widget.attrs['readonly'] = True
            self.fields['p1Time'].widget.attrs['readonly'] = True
            self.fields['p2Time'].widget.attrs['readonly'] = True
    
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {'flightDate': DateSelectorWidget,
                    'depTime': TimeSelectorWidget,
                    'arrTime': TimeSelectorWidget}
        # fields = ["flightDate", "flightNum",
        #         "tailNum", "coPilot", "depApt",
        #         "arrApt", "depTime", "arrTime",
        #         "pilotRole"]
