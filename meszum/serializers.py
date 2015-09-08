from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from meszum.models import Event

# Serializers define the API representation.
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'startdate', 'poster', 'address')

# ViewSets define the view behavior.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer