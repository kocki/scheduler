"""REST API views.

There is no security layer implemented. Should be added at least
for views allowing to change data.
"""

# 3rd-party
from events.models import Event
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id',
            'scheduled',
            'event_type',
            'event_data',
            'description',
            'created',
        )


class EventsViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.AllowAny,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
