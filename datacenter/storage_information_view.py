from datacenter.models import Visit
from django.shortcuts import render
from .models import Visit, get_duration, format_duration
import pytz


def storage_information_view(request):
    visits = Visit.objects.all()
    non_closed_visits = []
    local_tz = pytz.timezone("Europe/Moscow")
    for visit in visits:
        if visit.leaved_at is None and visit.entered_at is not None:
            dt_local = visit.entered_at.astimezone(local_tz)
            formatted_date = dt_local.strftime("%d %B %Y %H:%M")
            duration = get_duration(visits)
            formatted_duration = format_duration(duration)
            non_closed_visits.append({
                'who_entered': visit.passcard,
                'entered_at': formatted_date,
                'duration': formatted_duration,
            })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
