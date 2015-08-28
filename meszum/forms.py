from django import forms
from django.contrib.auth.models import Group
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

class SignupForm(forms.Form):
    isBussines = forms.CharField(max_length=2)

    def signup(self, request, user):
        if self.cleaned_data['isBussines'] == "1":
            group = Group.objects.get(name='Space')
        else:
            group = Group.objects.get(name='Member')
        user.groups.add(group)
        user.save()

# first_name = forms.CharField(max_length=30, label='Voornaam')
#     last_name = forms.CharField(max_length=30, label='Achternaam')
#
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
