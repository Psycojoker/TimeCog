import datetime

from datetime import date, timedelta

from .templates import Template
from django.template import Context

from events.models import Event

from cog import expose


@expose
def ensure_next_after_previous(state, kind, organisation, title, periodicity, minimum_from_today, acceptable_weekdays=range(7), number=1, time=None, locations=[]):
    events = Event.objects.filter(organisation=organisation, date__gte=date.today())

    # there are already events ready, don't do anything
    if events.exists():
        print "events already exists, don't do anything"
        return

    minimum_from_today_absolute = date.today() + timedelta(**minimum_from_today)

    previous_event_date = Event.objects.order_by('-date')

    periodicity = timedelta(**periodicity)

    if previous_event_date.exists():
        previous_event_date = previous_event_date.first().date
        candidate_date = previous_event_date + periodicity
    else:
        previous_event_date = None
        candidate_date = date.today() + timedelta(**minimum_from_today)

    while candidate_date < minimum_from_today_absolute:
        candidate_date += periodicity

    for i in range(number):
        while candidate_date.weekday() not in acceptable_weekdays:
            candidate_date += timedelta(days=1)

        event = Event()
        event.state = state
        event.organisation = organisation
        event.kind = kind
        event.date = candidate_date

        event_title = Template(title).render(Context({
            "event": event,
            "number_this_year": Event.objects.filter(organisation=organisation, kind=kind, date__year=date.today().year).count()
        }))

        print "Creating a new event '%s' for %s on %s state %s" % (event_title, organisation, candidate_date.strftime("%F"), state)

        if time:
            event.time = datetime.time(**time)

        event.save()

        candidate_date += timedelta(days=1)
