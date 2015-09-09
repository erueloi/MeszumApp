from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from meszum.models import Event

# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(source='startdate', read_only=True)
    class Meta:
        model = Event
        fields = ('id','title', 'description', 'start', 'poster', 'address')

# ViewSets define the view behavior.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer