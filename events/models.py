"""Database models for Event.

ToDo: extend with assigning user who made changes.
"""

# Django
from django.db import models


class EventType(models.Model):
    """Event types."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Event(models.Model):
    """Events storage.

    Assumed possibility to amend in plafce (on existing instance). When design needs to track
    changes we can extend it with e.g. with soft deletion: mark old data as deleted and provide
    new instance (with changes). There is still few objections related to functional design
    requirements.

    ?
    - Check, should it be timezone aware.
    """

    created = models.DateTimeField(auto_now_add=True, db_index=True, editable=False)
    scheduled = models.DateTimeField(db_index=True)
    event_type = models.ForeignKey(EventType, on_delete=models.DO_NOTHING)
    # Event data as storage for any additional data. In theory, in any desired format, but for
    # most cases, especially with PostgreSQL DB engine, JSON would be best choice (this field
    # should be changed to JsonField then):
    event_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.scheduled}/{self.event_type}'
