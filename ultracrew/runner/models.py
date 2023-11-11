from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

    
class Race(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateField()

class AidStation(models.Model):
    name = models.CharField(max_length=64)
    distance = models.FloatField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="stations")

class Checkpoints(models.Model):
    time = models.TimeField()
    runner = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(AidStation, on_delete=models.CASCADE)

class RaceRegistration(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="races")
    crew = models.ManyToManyField(User, related_name="crew_races")
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    minPace = models.DurationField() #pace in minutes per mile
    maxPace = models.DurationField()
    goalTime = models.DurationField() 