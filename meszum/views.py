from django.shortcuts import render
from django.contrib import messages
from meszum.forms import SpaceForm, EventForm, SubscribeForm, ProfileForm, UserProfileForm
from meszum.models import Space, Event, UserProfile
from django.contrib.auth.models import User
from geopy.geocoders.googlev3 import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError
from urllib2 import URLError
from django.contrib.gis import geos
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView, TemplateView

def geocode_address(address):
    address = address.encode('utf-8')
    geocoder = GoogleV3()
    try:
        _, latlon = geocoder.geocode(address)
    except (URLError, GeocoderQueryError, ValueError):
        return None
    else:
        point = "POINT(%s %s)" % (latlon[1], latlon[0])
        return geos.fromstr(point)

class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class SpaceFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'admin/modals/space_form.html'
    form_class = SpaceForm
    success_url = reverse_lazy('profilespace')
    success_message = "Way to go!"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        objUser = User.objects.get(id=self.request.user.id)
        objSpace = form.save(commit=False)
        objSpace.user = objUser
        objSpace.save()
        messages.add_message(
               self.request, messages.SUCCESS, 'Logged in Successfully')
        messages.success(self.request,'Space added successfully')
        return super(SpaceFormView, self).form_valid(form)

def commingsoon(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        data = {}
        # Send email with activation key
        if request.is_ajax():
            if form.is_valid():
                form.save(commit=True)
                #send mail
                subject = 'Subscribe Meszum Stay up-to-date'
                text_content = 'Thanks for subscribing Meszum App! As soon as we are ready to accepts registrations we will send you an email in order to inform you. See you soon ;),'
                html_content = get_template('email/stay_up_date.html').render()
                from_email = '"Meszum" <hello@meszum.com>'
                to = form.cleaned_data['email']
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.content_subtype = 'html'
                msg.send()

                data['valid'] = '1'
                data['message'] = 'Thanks for your subscription!'
                return JsonResponse(data)
            else:
                data['valid'] = '0'
                data['message'] = 'Insert a valid email address!'
                return JsonResponse(data)
    #Get goes here
    return render(request, 'commingsoon.html')

def startpage(request):
    # if request.method == 'POST':
    #     form = SubscribeForm(request.POST)
    #     # Send email with activation key
    #     if form.is_valid():
    #         form.save(commit=True)
    #         email_subject = 'Subscribe Meszum Stay up-to-date'
    #         email_body = "Thanks to subscribe Meszum App. When our application is ready to register will send an email to inform you. See you soon ;),"
    #         email_address = form.cleaned_data['email']
    #         send_mail(email_subject, email_body, 'hello@meszum.com',
    #             [email_address], fail_silently=False)
    #         messages.success(request, 'Email sent successfully. Thank you for subscribe.')
    # else:
    #     form = SubscribeForm()

    return render(request, 'startpage.html',  {})

def index(request):
    context_dict = {}
    context_dict['events'] = Event.objects.all();
    return render(request, 'index.html', context_dict)

def superuserdashboard(request):
    context_dict = {}
    context_dict['nspaces'] = Space.objects.all().count();
    context_dict['nusers'] = User.objects.all().count();
    context_dict['nevents'] = Event.objects.all().count();
    return render(request, 'admin/superuser_dashboard.html', context_dict)

def sd_spaces(request):
    context_dict = {}
    context_dict['spaces'] = Space.objects.all();
    return render(request, 'admin/sd_spaces.html', context_dict)

def sd_users(request):
    context_dict = {}
    context_dict['users'] = User.objects.all();
    return render(request, 'admin/sd_users.html', context_dict)

class EventFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'admin/modals/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('profilespace')
    success_message = "Way to go!"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        objUser = User.objects.get(id=self.request.user.id)
        try:
            objSpace = Space.objects.get(id=form.data['spaceid'])
        except Space.DoesNotExist:
            objSpace = None
        address = form.cleaned_data['address']
        objEvent = form.save(commit=False)
        objEvent.geometry = geocode_address(address)
        objEvent.space = objSpace
        objEvent.save()

        messages.add_message(
               self.request, messages.SUCCESS, 'Logged in Successfully')
        messages.success(self.request,'Space added successfully')
        return super(EventFormView, self).form_valid(form)

def administrationspace(request, idspace):
    context_dict = {}
    try:
        objSpace = Space.objects.get(id=idspace)
    except Space.DoesNotExist:
        objSpace = None

    context_dict['space'] = objSpace
    context_dict['events'] = Event.objects.filter(space=objSpace)

    # A HTTP POST?
    if request.method == 'POST':
        form = SpaceForm(request.POST, request.FILES, instance=objSpace)
        if form.is_valid():
            objSpace = form.save(commit=False)
            objUser = User.objects.get(id=request.user.id)
            objSpace.user = objUser
            objSpace.save()
            messages.add_message(request, messages.SUCCESS, 'S''ha guardat correctament')
        else:
            print form.errors
    else:
        form = SpaceForm(instance=objSpace)

    context_dict['form'] = form

    return render(request, 'admin/space.html', context_dict)

def profilespace(request):
    context_dict = {}
    objUser = User.objects.get(id=request.user.id)
    objUserProfile = UserProfile.objects.get(user=objUser)
    context_dict['profile'] = objUserProfile
    context_dict['spaces'] = Space.objects.filter(user=objUser)
    nspace = 0
    for objspace in objUser.space_set.all():
        nspace = nspace + objspace.event_set.all().count()
    context_dict['nevents'] = nspace
    #objSpace = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=objUserProfile)
        formuser = ProfileForm(request.POST, instance=objUser)
        #formspace = SpaceForm(request.POST, request.FILES, instance=objSpace)
        if form.is_valid() and formuser.is_valid():
            form.save()
            formuser.save()
            messages.success(request,'Profile updated successfully')
        # if formspace.is_valid():
        #     objSpace = formspace.save(commit=False)
        #     objSpace.user = objUser
        #     objSpace.save()
        #     messages.success(request,'Event added successfully')
    else:
        form = UserProfileForm(request.FILES, instance=objUserProfile)
        formuser = ProfileForm(instance=objUser)
        #formspace = SpaceForm(request.FILES, instance=objSpace)

    context_dict['form'] = form
    context_dict['formuser'] = formuser
    #context_dict['formspace'] = formspace

    return render(request, 'account/profilespace.html', context_dict)

def administrationevents(request, idspace):
    context_dict = {}
    try:
        space = Space.objects.get(id=idspace)
        events = Event.objects.filter(space=space).order_by('startdate')
    except Space.DoesNotExist:
        space = None
        events = None

    context_dict['space'] = space
    context_dict['events'] = events

    return render(request, 'admin/events.html', context_dict)

def addevents(request, idspace, idevent=None):
    context_dict = {}
    try:
        objSpace = Space.objects.get(id=idspace)
    except Space.DoesNotExist:
        objSpace = None

    if idevent:
        oEvent = Event.objects.get(id=idevent)
    else:
        oEvent = None

    context_dict['space'] = objSpace

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=oEvent)
        if form.is_valid():
            address = form.cleaned_data['address']
            objEvent = form.save(commit=False)
            objEvent.geometry = geocode_address(address)
            objEvent.space = objSpace
            objEvent.save()
            #Save Event
            messages.success(request,'S''ha guardat correctament l''Event')
            return administrationspace(request, idspace)
        else:
            print form.errors
    else:
        form = EventForm(instance=oEvent)



    context_dict['event'] = oEvent
    context_dict['form'] = form
    return render(request, 'admin/addevents.html', context_dict)

def profile(request):
    context_dict = {}
    objUser = User.objects.get(id=request.user.id)
    objUserProfile = UserProfile.objects.get(user=objUser)
    context_dict['profile'] = objUserProfile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        formprofile = UserProfileForm(request.POST, request.FILES, instance=objUserProfile)
        if form.is_valid() and formprofile.is_valid():
            form.save()
            formprofile.save()
            messages.success(request,'Profile updated successfully')
    else:
        form = ProfileForm(instance=request.user)
        formprofile = UserProfileForm(request.FILES, instance=objUserProfile)

    context_dict['formprofile'] = formprofile
    context_dict['form'] = form

    return render(request, 'account/profile.html', context_dict)

#This class holds the tweet - it's structured
# on purpose so we can easily access elements in
# a template tag
class tweet():
    def __init__(self, user, text, graphic, time):
        self.user = user
        self.text = text
        self.graphic = graphic
        self.time = time

# The meat of the operation
def search_twitter():
    search_url = 'http://search.twitter.com/search.json?q=Django'
    import simplejson as json
    import urllib

    raw = urllib.urlopen(search_url)
    js = raw.readlines()
    js_object = json.loads(js[0])

    #filter it all
    tweets = []
    for item in js_object['results']:
        user = item['from_user']
        graphic = item['profile_image_url']
        text = item['text']
        time = item['created_at']

        thistweet = tweet(user, text, graphic, time)
        tweets.append(thistweet)

    return tweets
