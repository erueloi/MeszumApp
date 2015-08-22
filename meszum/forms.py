from django import forms
from meszum.models import Space, Event

class SpaceForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    logotype = forms.ImageField(required=False)

    class Meta:
        model = Space
        fields = ('name', 'email', 'logotype')

class EventForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    startdate = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y%"))
    poster = forms.ImageField(required=True)
    address = forms.CharField(max_length=100)

    class Meta:
        model = Event
        fields = ('title', 'description', 'startdate', 'poster', 'address')

