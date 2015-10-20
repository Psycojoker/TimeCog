from datetime import date
from events.models import Event

from cog import expose


@expose
def ensure_next_after_previous(state, organisation, periodicity, minimum_from_today, acceptable_weekdays=range(1, 8), number=1, time=None):
    events = Event.objects.filter(organisation=organisation, date__gte=date.today())

    # there are already events ready, don't do anything
    if events.exists():
        return
