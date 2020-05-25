# Django
from django.contrib import admin

# 3rd-party
from events.models import Event
from events.models import EventType


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'description',
    )
    search_fields = (
        'name',
        'description',
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'scheduled',
        'event_type',
        'event_data',
        'description',
        'created',
    )
