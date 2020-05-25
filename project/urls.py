"""Project URL Configuration"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path

api_patterns = (
    [
        path('events/', include('events.urls')),
    ], 'api')

urlpatterns = [
    path('api/', include(api_patterns)),
    url(r'^admin/', admin.site.urls),
]
