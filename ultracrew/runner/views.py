from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Race, AidStation, RaceRegistration
from .forms import RaceForm, RaceRegistrationForm, AidStationForm, StationForms
from django.views.generic import ListView, TemplateView

#https://nadchif.github.io/html-duration-picker.js/
#https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript


class StationListView(ListView):
    model = AidStation
    template_name = "runner/station_list.html"


class StationAddView(TemplateView):
    template_name = "runner/add_station.html"

    def get(self, *args, **kwargs):
        formset = StationForms(queryset=AidStation.objects.none())
        return self.render_to_response({'station_formset': formset})
    
    def post(self, *args, **kwargs):
        formset = StationForms(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect()
        return self.render_to_response({'station_formset': formset})

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