from django import forms
from meszum.models import Space, Event

class SpaceForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    logotype = forms.ImageField(required=False)

    class Meta:
        model = Space
        fields = ('name', 'email', 'logotype')

