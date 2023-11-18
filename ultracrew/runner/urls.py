from django.urls import path
from . import views


app_name = 'runner'

urlpatterns = [
    path("addrace", views.addRace, name="addRace"),
    path("crew", views.crewPage, name="crewPage"),
    path("<str:name>",views.runnerPage, name="runnerPage"),
    path("", views.homepage, name="homepage"),
    #path("addrace/add", StationAddView, name="add_station"),
    #path("addrace/", StationListView, name="station_list")
]