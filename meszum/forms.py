from django import forms
from django.contrib.auth.models import Group, User
from meszum.models import Space, Event, Subscriber, UserProfile

class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Subscriber
        fields = ('email',)

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
    startdate = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))
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
        objUserProfile = UserProfile()
        objUserProfile.user = user
        objUserProfile.save()

class ProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('avatar',)