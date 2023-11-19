from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.forms import modelformset_factory
from .models import Race, AidStation, RaceRegistration, Checkpoint
from .forms import RaceForm, RaceRegistrationForm, AidStationForm#, StationFormSet
from django.views.generic import ListView, TemplateView
from django.conf import settings
from django.contrib.auth.models import User
import datetime

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

def crewPage(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login")
    crewRaces = request.user.crew_races.all()
    return render(request, "runner/crew.html", {"crewRaces":crewRaces})

def runnerPage(request, name):
    # TODO authentication
    participant = get_user(name)
    if participant == None:
        return render(request, "runner/crew.html")
    
    #recieve a logged checkpoint
    if request.method == "POST":
        #try: 
        checkpoint = Checkpoint(runner=participant, station = AidStation.objects.get(pk = request.POST["station"]))
        poster = request.user
        
        # Distinguish between loggers and only allow self or crew to log aid stations
        if checkpoint.runner.races.filter(race=checkpoint.station.race).exists():
            if checkpoint.runner.races.get(race=checkpoint.station.race).crew.filter(id = poster.id).exists():
                # crew
                checkpoint.save()
            elif poster == checkpoint.runner:
                # self 
                checkpoint.save()
            else:
                # unauthorized
                return HttpResponseForbidden("You are not listed as crew for that runner. Please confirm that you are logged in and are viewing the correct runner.")

        else:
            print("nope")
        #except:
        #    print("error")
        #else:
        
        return redirect(request.META.get('HTTP_REFERER'))

    
    # For GET
     
    registrations = participant.races.all().order_by("race__date")
    races = []
    for registration in registrations:

        # find logged checkpoints at aid stations of the given race
        isCrewOrSelf = registration.crew.filter(id = request.user.id).exists() or request.user == participant
        stations = registration.race.stations.all().order_by('distance')
        stationsLog = []
        for station in stations:
            thisStationLog = {"station": station, "time": None, "prediction": None, "goalTarget": None, "authorized": isCrewOrSelf, "splitPace": None}
            if participant.checkpoints.filter(station=station).exists():
                thisStationLog["time"] = participant.checkpoints.get(station=station).time
            stationsLog.append(thisStationLog)
        
        # Calculate predicted times based on pace between last two aid stations, if available
        
        startTime = datetime.datetime.combine(registration.race.date, registration.race.startTime)
        if(stationsLog[0]["time"] and stationsLog[0]["station"].distance == 0):
            startTime = stationsLog[0]["time"]
            
        paceForGoal = registration.race.totalDistance / registration.goalTime.total_seconds()

        pace = None
        lastLog = None
        for i in range(len(stationsLog)):
            
            thisLog = stationsLog[i]

            deltaSecondsGoal = thisLog["station"].distance / paceForGoal
            deltaTimeGoal = datetime.timedelta(seconds = deltaSecondsGoal)
            stationsLog[i]["goalTarget"] = startTime + deltaTimeGoal

            if thisLog["time"]:
                if lastLog:
                    if(thisLog["time"] > lastLog["time"]):
                        pace = (thisLog["station"].distance - lastLog["station"].distance) / ((thisLog["time"] - lastLog["time"]).total_seconds())
                        stationsLog[i]["splitPace"] = pace
                lastLog = thisLog
            else:
                if pace and lastLog:
                    deltaSeconds = (thisLog["station"].distance - lastLog["station"].distance) / pace
                    deltaTime = datetime.timedelta(seconds = deltaSeconds)
                    stationsLog[i]["prediction"] = lastLog['time'] + deltaTime
                    print(stationsLog[i])
                    


        race ={
               "registration": registration,
               "stationsLog": stationsLog,
                
        }
        
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
            # The Duck Debugger helped me with this code to turn usernames into users for the many to many field
            registration.save()
            usernames = regform.cleaned_data['crew_usernames']
            for username in usernames:
                user = User.objects.get(username=username)  # get User instance
                registration.crew.add(user)  # add User to crew

            stations = stationforms.save(commit=False)
            print(stations)
            for station in stations:
                station.race = race
                station.save()
            return redirect(reverse("runner:runnerPage", args= [request.user.username]))
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