from django.urls import path
from . import views
from .views import StationAddView, StationListView

app_name = 'runner'

urlpatterns = [
    #path("addrace/", views.addRace, name="addRace/"),
    path("addrace", views.addRace, name="addRace"),
    path("dashboard/", views.dashboard, name="dashboard/"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("<str:name>",views.runnerPage, name="runnerPage"),
    path("", views.homepage, name="homepage"),
    path("addrace/add", StationAddView, name="add_station"),
    path("addrace/", StationListView, name="station_list")
]