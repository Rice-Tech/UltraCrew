from django.urls import path
from . import views

app_name = 'runner'

urlpatterns = [
    path("addrace/", views.addRace, name="addRace/"),
    path("addrace", views.addRace, name="addRace"),
    path("dashboard/", views.dashboard, name="dashboard/"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("<str:name>",views.runnerPage, name="runnerPage"),
]