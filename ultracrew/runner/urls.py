from django.urls import path
from . import views


app_name = 'runner'

urlpatterns = [
    path("addrace", views.addRace, name="addRace"),
    path("crew", views.crewPage, name="crewPage"),
    path("<str:name>",views.runnerPage, name="runnerPage"),

]