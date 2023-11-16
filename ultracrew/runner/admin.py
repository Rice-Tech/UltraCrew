from django.contrib import admin
from .models import Race, RaceRegistration, AidStation, Checkpoint
# Register your models here.
admin.site.register(Race)
admin.site.register(RaceRegistration)
admin.site.register(AidStation)
admin.site.register(Checkpoint)