# Django
from django.urls import re_path

# 3rd-party
from events.consumers import EventConsumer

websocket_urlpatterns = [
    re_path(r'ws/events/$', EventConsumer),
]
