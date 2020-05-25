# Django
from django.urls import include
from django.urls import path

# 3rd-party
from rest_framework import routers

from events.views import EventsViewSet

router = routers.DefaultRouter()
router.register('', EventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
