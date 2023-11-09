from django.shortcuts import render, redirect
from django.views.generic import ListView
from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Race, AidStation, RaceRegistration


#https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript

class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'date']

class RaceRegistrationForm(ModelForm):
    class Meta:
        model = RaceRegistration
        fields = ['minPace', 'maxPace', 'goalTime', 'crew']


class AidStationForm(ModelForm):
    class Meta:
        model: AidStation
        fields: ['name', 'distance']

StationForms = modelformset_factory(AidStation, AidStationForm, fields= ['name', 'distance'], extra=1, max_num=20)

class FullForm(forms.Form):
    race = RaceForm()
    raceRegistration = RaceRegistrationForm()
    stations = StationForms(prefix="station")

# views

def dashboard(request):
    return render(request, "runner/dashboard.html")

def runnerPage(request, name):
    return render(request, "runner/runnerPage.html", {'name':name})

def addRace(request):
    if request.method == "POST":
        #Validate data and rearange to desired format
        raceform = FullForm(request.POST, prefix='raceform')
        if raceform.is_valid():
            return redirect("/runner/" + raceform.name)
        
    else:
        raceform = FullForm(prefix='raceform')    

    return render(request, "runner/addRace.html", {"raceform":raceform})

def homepage(request):
    return render(request, "home.html")