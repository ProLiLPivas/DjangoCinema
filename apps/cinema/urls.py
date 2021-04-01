from django.urls import path
from .views import *


urlpatterns = [
    path('', CinemaList.as_view(), name='cinema_list_url'),

    path('create/', CinemaCreate.as_view(), name='cinema_create_url'),
    path('<int:pk>/update/', CinemaUpdate.as_view(), name='cinema_update_url'),
    path('<int:pk>/delete/', CinemaDelete.as_view(), name='cinema_delete_url'),

    path('<int:pk>/', CinemaDetail.as_view(), name='cinema_url'),

    path('<int:pk>/hall/all/', CinemaHallsDetail.as_view(), name='cinema_url'),
    path('<int:pk>/hall/create/', CreateHall.as_view(), name='hall_create_url'),

    path('hall/<int:pk>/', DetailHall.as_view(), name='hall_url'),
    path('hall/<int:pk>/edit/', UpdateHall.as_view(), name='hall_edit_url'),
    path('hall/<int:pk>/delete/', DeleteHall.as_view(), name='hall_delete_url'),
    path('hall/<int:pk>/copy/', CopyHall.as_view(), name='hall_copy_url'),
]




