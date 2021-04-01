from django.http import QueryDict

from apps.schedules.models import ScheduleDay, Seance


def get_schedule_to_context(day: ScheduleDay = None, seances: QueryDict = None) -> dict:
    films_seances = {}

    if not seances and not day and len(seances) != 0:
        seances = Seance.objects.filter()
    elif not seances:
        seances = Seance.objects.filter(day=day)

    for seance in seances:
        if not films_seances.get(seance.film):
            films_seances.update({seance.film: [seance]})
        else:
            films_seances[seance.film].append(seance)

    return films_seances
