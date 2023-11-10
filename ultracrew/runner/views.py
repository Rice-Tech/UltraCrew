from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import AidStation
from .forms import RaceForm, RaceRegistrationForm, AidStationForm

#https://nadchif.github.io/html-duration-picker.js/
#https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript

StationForms = modelformset_factory(AidStation, AidStationForm, fields= ['name', 'distance'], extra=1, max_num=20)

# views

def dashboard(request):
    return render(request, "runner/dashboard.html")

def runnerPage(request, name):
    return render(request, "runner/runnerPage.html", {'name':name})

def addRace(request):
    if request.method == "POST":
        #Validate data and rearange to desired format
        #fullForm = FullForm(request.POST, prefix='fullForm')
        raceform = RaceForm(request.POST, prefix="race")
        regform = RaceRegistrationForm(request.POST, prefix="reg")
        stationforms = StationForms(request.POST, prefix="station")
        if raceform.is_valid() and regform.is_valid and stationforms.is_valid:
            if raceform.is_valid():
                print(raceform.cleaned_data['name'])
            else:
                print("Invalid!!!")
                #fullForm.race = raceform
            #print(raceform)
            #return redirect("/runner/" + raceform.name)
        
    else:
        raceform = RaceForm(prefix="race")
        regform = RaceRegistrationForm(prefix="reg")
        stationforms = StationForms(prefix="station")
        
        #fullForm = FullForm(prefix='fullForm')    

    return render(request, "runner/addRace.html", {"raceform":raceform, "regform":regform, "stationforms":stationforms})

def homepage(request):
    return render(request, "home.html")