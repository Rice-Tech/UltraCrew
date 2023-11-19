from django.forms import ModelForm, modelformset_factory
from .models import Race, AidStation, RaceRegistration
from django import forms
from django.contrib.auth.models import User

class RaceForm(ModelForm):
    name = forms.CharField(label= "Race Name", widget=forms.TextInput(attrs= {'placeholder':'eg. Stone Mill 50 Mile'}))
    totalDistance = forms.FloatField(label = "Race Distance", widget=forms.NumberInput(attrs = {'placeholder': "Distance in miles", 'min':0.1, 'step':0.1}))
    startTime = forms.TimeField(label = "Scheduled Start Time", widget= forms.TimeInput(attrs={'type':'time'}))
    class Meta:
        model = Race
        fields = ['name', 'date', 'startTime', 'totalDistance']
        widgets = {
            #'name': forms.TextInput(attrs={'type': 'text'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class RaceRegistrationForm(ModelForm):
    crew_usernames = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'friend1, friend2'}))
    goalTime = forms.CharField(label='Goal Time', widget=forms.TextInput(attrs={'class':'html-duration-picker'}))
    class Meta:
        model = RaceRegistration
        fields = ['goalTime']
        
    def clean_crew_usernames(self):
        data = self.cleaned_data['crew_usernames']
        usernames = data.split(',')
        users = []
        for username in usernames:
            username = username.strip()
            try:
                user = User.objects.get(username=username)
                users.append(user)
            except User.DoesNotExist:
                self.add_error('crew_usernames', 'User ' + username + ' does not exist')
        return users


class AidStationForm(ModelForm):
    class Meta:
        model: AidStation
        fields: ['name', 'distance']

StationFormSet = modelformset_factory(AidStation, fields= ['name', 'distance'], extra=7, max_num=20)