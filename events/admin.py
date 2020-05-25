from django.contrib import admin

from events.models import EventType, Event


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
