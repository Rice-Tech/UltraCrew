from django.shortcuts import render, redirect, HttpResponse
from django.forms import modelformset_factory
from .models import Race, AidStation, RaceRegistration
from .forms import RaceForm, RaceRegistrationForm, AidStationForm#, StationFormSet
from django.views.generic import ListView, TemplateView
from django.conf import settings
from django.contrib.auth.models import User

#User = settings.AUTH_USER_MODEL

#https://nadchif.github.io/html-duration-picker.js/
#https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript

'''
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
'''
# views

def dashboard(request):
    return render(request, "runner/dashboard.html")

def runnerPage(request, name):
    # TODO authentication
    participant = get_user(name)
    if participant == None:
        return render(request, "runner/dashboard.html")
  
    registrations = participant.races.all()
    races = []
    for registration in registrations:
        race ={"name": registration.race.name,
               "date": registration.race.date, 
               "stations":registration.race.stations.all()}
       
        print(race['stations'])
        races.append(race) 
    return render(request, "runner/runnerPage.html", {'name':name, 'races':races})

def addRace(request):
    StationFormSet = modelformset_factory(AidStation, fields=['name', 'distance'], extra=3, max_num=20)
    if request.method == "POST":
        #Validate data and rearange to desired format
        #fullForm = FullForm(request.POST, prefix='fullForm')
        raceform = RaceForm(request.POST, prefix="race")
        regform = RaceRegistrationForm(request.POST, prefix="reg")
        
        stationforms = StationFormSet(request.POST, prefix="station")
        if raceform.is_valid() and regform.is_valid() and stationforms.is_valid():
            race = raceform.save()
            registration = regform.save(commit=False)
            registration.race = race
            registration.participant =  request.user
            registration.save()
            stations = stationforms.save(commit=False)
            print(stations)
            for station in stations:
                station.race = race
                station.save()
                print(station)
            return redirect("/runner/dashboard")
        else:
            print("Invalid!!!")
            print(regform.is_valid())
            print(stationforms.is_valid())
            #fullForm.race = raceform
            #print(raceform)
            #return redirect("/runner/" + raceform.name)
        
    else:
        
        raceform = RaceForm(prefix="race")
        regform = RaceRegistrationForm(prefix="reg")
        stationforms = StationFormSet(queryset=AidStation.objects.none(), prefix="station")
        
        #fullForm = FullForm(prefix='fullForm')    

    return render(request, "runner/addRace.html", {"raceform":raceform, "regform":regform, "stationforms":stationforms})

def homepage(request):
    return render(request, "home.html")

def get_user(name):
    try:
        user = User.objects.get(username=name)
    except User.DoesNotExist:
        user = None
    return user