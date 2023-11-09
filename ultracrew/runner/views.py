from django.shortcuts import render, redirect
from django import forms
from django.forms import formset_factory

class StationForm(forms.Form):
    name = forms.CharField(max_length=64)
    distance = forms.FloatField()

StationForms = formset_factory(StationForm, extra=7, max_num=20)

#https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript

class RaceForm(forms.Form):
    name = forms.CharField(max_length=64)
    date = forms.DateField()
    stations = StationForms(prefix='station')
    #formset_factory(stationForm, extra=1, max_num=20)


# Create your views here.

def dashboard(request):
    return render(request, "runner/dashboard.html")

def runnerPage(request, name):
    return render(request, "runner/runnerPage.html", {'name':name})

def addRace(request):
    if request.method == "POST":
        #Validate data and rearange to desired format
        raceform = RaceForm(request.POST, prefix='raceform')
        if raceform.is_valid():
            return redirect("/runner/" + raceform.name)
        
    else:
        raceform = RaceForm(prefix='raceform')    

    return render(request, "runner/addRace.html", {"raceform":raceform})

def homepage(request):
    return render(request, "home.html")