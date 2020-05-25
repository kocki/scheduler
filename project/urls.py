"""Project URL Configuration"""

# Django
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

api_patterns = (
    [
        path('events/', include('events.urls')),
    ], 'api')

urlpatterns = [
    path('api/', include(api_patterns)),
    path('', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
]
