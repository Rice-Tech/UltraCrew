from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "runner/dashboard.html")

def runnerPage(request, name):
    return render(request, "runner/runnerPage.html", {'name':name})

def addRace(request):
    return render(request, "runner/addRace.html")