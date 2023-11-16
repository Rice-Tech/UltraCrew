from django.forms import ModelForm, modelformset_factory
from .models import Race, AidStation, RaceRegistration
from django import forms
from django.contrib.auth.models import User

class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'date']
        widgets = {
            'name': forms.NumberInput(attrs={'type': 'text'}),
            'date': forms.TextInput(attrs={'type': 'date'}),
        }

class RaceRegistrationForm(ModelForm):
    crew_usernames = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'friend1, friend2'}))
    class Meta:
        model = RaceRegistration
        fields = ['minPace', 'maxPace', 'goalTime']
        widgets = {
            'minPace': forms.TextInput(attrs={'class':'html-duration-picker'}),
            'maxPace': forms.TextInput(attrs={'class':'html-duration-picker'}),
            'goalTime': forms.TextInput(attrs={'class':'html-duration-picker'}),
        }
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