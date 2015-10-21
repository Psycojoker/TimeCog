import datetime

from datetime import date, timedelta

from events.models import Event

from cog import expose


@expose
def ensure_next_after_previous(state, organisation, title, periodicity, minimum_from_today, acceptable_weekdays=range(7), number=1, time=None):
    events = Event.objects.filter(organisation=organisation, date__gte=date.today())

    # there are already events ready, don't do anything
    if events.exists():
        print "events already exists, don't do anything"
        return

    minimum_from_today = date.today() + timedelta(**minimum_from_today)

    previous_event_date = Event.objects.order_by('-date')

    periodicity = timedelta(**periodicity)

    if previous_event_date.exists():
        previous_event_date = previous_event_date.first().date
        candidate_date = previous_event_date + periodicity
    else:
        previous_event_date = None
        candidate_date = date.today()

    while candidate_date < minimum_from_today:
        candidate_date += periodicity

    for i in range(number):
        while candidate_date.weekday() not in acceptable_weekdays:
            candidate_date += timedelta(days=1)

        print "Creating a new event for %s on %s state %s" % (organisation, candidate_date.strftime("%F"), state)
        event = Event()
        event.state = state
        event.organisation = organisation
        event.date = candidate_date

        if time:
            event.time = datetime.time(**time)

        event.save()

        candidate_date += timedelta(days=1)
