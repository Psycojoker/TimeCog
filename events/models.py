import uuid
from django.db import models


class Event(models.Model):
    organisation = models.CharField(max_length=255)

    kind = models.CharField(max_length=255)

    title = models.CharField(max_length=255)
    date = models.DateField()
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

    def __unicode__(self):
        return "[%s:%s:%s] %s on %s" % (self.organisation, self.kind, self.state, self.title, self.date.strftime("%F"))


class EmailQuestion(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    event = models.ForeignKey(Event)
    sent = models.DateTimeField(auto_now_add=True)

    questions = models.TextField()
