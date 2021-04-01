from django.urls import path
from .views import *


urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule_url'),

    path('day=<int:day_slug>/',
        ScheduleDayDetail.as_view(), name='schedule_day_url'),

    path('day=<int:day_slug>/film=<int:film_id>/add/',
         AddSeanceView.as_view(), name='add_seance_url'),

    path('day=<int:day_slug>/film=<int:film_id>/del/',
         DeleteFilmSeanceView.as_view(), name='delete_film_seance_url'),

    path('seance=<int:seance_id>/',
         SeanceDetail.as_view(), name='seance_url'),

    path('seance=<int:seance_id>/upd/',
         UpdateSeanceView.as_view(), name='update_seance_url'),

    path('seance=<int:seance_id>/del/',
         DeleteSeanceView.as_view(), name='delete_seance_url'),
]
