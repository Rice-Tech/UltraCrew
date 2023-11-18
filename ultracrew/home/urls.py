from django.urls import path
from . import views

app_name = 'runner'

urlpatterns = [
    path("", views.HomePageView, name="home"),
    
]