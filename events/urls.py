# Django
from django.urls import include
from django.urls import path

# 3rd-party
from events.views import EventsViewSet, EventTypesViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('types', EventTypesViewSet)
router.register('', EventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
