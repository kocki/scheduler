"""REST API views.

There is no security layer implemented. Should be added at least
for views allowing to change data.
"""

# 3rd-party
from events.models import Event, EventType
from rest_framework import filters
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets


class EventTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = (
            'id',
            'name',
            'description',
        )


class EventTypesViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = EventType.objects.all().order_by('name')
    serializer_class = EventTypeSerializer


class EventSerializer(serializers.ModelSerializer):

    event_type_id = serializers.IntegerField()

    class Meta:
        model = Event
        fields = (
            'id',
            'scheduled',
            'event_type_id',
            'event_data',
            'description',
            'created',
        )


class EventsViewSet(viewsets.ModelViewSet):

    filter_backends = [filters.SearchFilter]
    permission_classes = (permissions.AllowAny,)
    queryset = Event.objects.all().order_by('-scheduled')
    search_fields = (
        'description',
        'event_data',
        'event_type__name',
        'event_type__description',
    )
    serializer_class = EventSerializer
