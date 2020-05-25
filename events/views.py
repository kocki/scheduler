"""REST API views.

There is no security layer implemented. Should be added at least
for views allowing to change data.
"""

from rest_framework import viewsets, permissions, serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
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
