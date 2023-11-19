from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator

User = settings.AUTH_USER_MODEL

# Create your models here.

    
class Race(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateField()
    startTime = models.TimeField()
    totalDistance = models.FloatField(validators=[MinValueValidator(0.1)])
class AidStation(models.Model):
    name = models.CharField(max_length=64)
    distance = models.FloatField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="stations")

class Checkpoint(models.Model):
    time = models.DateTimeField(default=timezone.now)
    runner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checkpoints")
    station = models.ForeignKey(AidStation, on_delete=models.CASCADE)

class RaceRegistration(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="races")
    crew = models.ManyToManyField(User, related_name="crew_races")
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    #minPace = models.DurationField() #pace in minutes per mile
    #maxPace = models.DurationField()
    goalTime = models.DurationField() 