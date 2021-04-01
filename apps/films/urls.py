from django.urls import path
from .views import *



urlpatterns = [
    path('all/', FilmsListView.as_view(), name='film_list_url'),
    path('<int:pk>/', FilmDetail.as_view(), name='about_film_url'),
    path('create/', CreateFilm.as_view(), name='create_film_url') ,
    path('<int:pk>/update/', UpdateFilm.as_view(), name='update_film_url') ,
    path('<int:pk>/delete/', DeleteFilm.as_view(), name='delete_film_url') ,

    path('person/create/', CreatePerson.as_view(), name='create_person_url'),
    path('person/<int:pk>/', PersonDetail.as_view(), name='about_person_url'),
    path('person/<int:pk>/update/', UpdatePerson.as_view(), name='update_person_url'),
    path('person/<int:pk>/delete/', DeletePerson.as_view(), name='delete_person_url'),

    path('genre/create/' , CreateGenre.as_view(), name='create_genre_url'),
    path('genre/<int:pk>/', GenreDetail.as_view(), name='about_genre_url'),
    path('genre/<int:pk>/update/', UpdateGenre.as_view(), name='update_genre_url'),
    path('genre/<int:pk>/delete/', DeleteGenre.as_view(), name='delete_genre_url'),

    path('role/create/', CreateRole .as_view(), name='create_role_url'),
    path('role/<int:pk>/', RoleDetail.as_view(), name='about_role_url'),
    path('role/<int:pk>/update/', UpdateRole.as_view(), name='update_role_url'),
    path('role/<int:pk>/delete/', DeleteRole.as_view(), name='delete_role_url'),
    # path('genre/', GenreDetail.as_view(), ),
]
