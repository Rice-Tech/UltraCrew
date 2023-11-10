from django.forms import ModelForm, modelformset_factory
from .models import Race, AidStation, RaceRegistration
from django import forms

class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'date']
        widgets = {
            'name': forms.NumberInput(attrs={'type': 'text'}),
            'date': forms.TextInput(attrs={'type': 'date'}),
        }

class RaceRegistrationForm(ModelForm):
    class Meta:
        model = RaceRegistration
        fields = ['minPace', 'maxPace', 'goalTime', 'crew']
        widgets = {
            'minPace': forms.TextInput(attrs={'class':'html-duration-picker'}),
            'maxPace': forms.TextInput(attrs={'class':'html-duration-picker'}),
            'goalTime': forms.TextInput(attrs={'class':'html-duration-picker'}),
        }


class AidStationForm(ModelForm):
    class Meta:
        model: AidStation
        fields: ['name', 'distance']