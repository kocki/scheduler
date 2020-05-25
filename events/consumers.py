# Django
from django.db.models import signals
from django.dispatch import receiver

# 3rd-party
import channels.layers
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from events.models import Event

ACTIONS = {
    True: 'New event',
    False: 'Event updated',
    None: 'Event deleted',
}


class EventConsumer(JsonWebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name,
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'events',
            self.channel_name,
        )
        self.close()

    def receive_json(self, content, **kwargs):
        print(f'Received event: {content}')

    def events_alarm(self, event):
        self.send_json(event['data'])

    @staticmethod
    @receiver(signals.post_save, sender=Event)
    @receiver(signals.post_delete, sender=Event)
    def events_observer(sender, instance, **kwargs):
        action = ACTIONS[kwargs.get('created')]
        layer = channels.layers.get_channel_layer()
        async_to_sync(layer.group_send)('events', {
            'type': 'events.alarm',
            'data': {
                'action': action,
                'id': instance.pk,
            },
        })
