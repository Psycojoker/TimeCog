from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    private_comments = models.TextField(null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)

    EVENT_STATES = (
        ('proposition', 'Proposition'),
        ('canceled', 'Canceled'),
        ('planned', 'Planned'),
        ('public', 'Public'),
    )

    state = models.CharField(max_length=255, choices=EVENT_STATES)
