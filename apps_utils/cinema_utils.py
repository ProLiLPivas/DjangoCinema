from random import randint
from typing import Union, List

from django.db.models import Q
from django.http import QueryDict

from apps.cinema.models import Cinema
from apps.films.models import Film
from apps.schedules.models import Seance, ScheduleDay


def get_cinema_seances(cinema: Cinema, today: bool = False) -> QueryDict:
    if today:
        dayQ = Q(day=ScheduleDay.get_today_schedule_obj())
    else:
        dayQ = Q(day__slug__gte=ScheduleDay.get_today_schedule_slug())

    return Seance.objects.filter(
        Q(hall__cinema=cinema) &
        Q(film__is_showing=True) &
        dayQ
    )


def get_cinema_films(cinema: Cinema) -> List[Film]:
    cinema_seances = get_cinema_seances(cinema)
    return [seance.film for seance in cinema_seances]


def get_random_posters_to_slider(films: Union[list, QueryDict], amount=3) -> list:
    film_nums = set()
    while len(film_nums) < amount or len(film_nums) < len(films):
        film_nums.add(randint(0, len(films) - 1))
    return [films[film_nums].poster for film_nums in list(film_nums)]