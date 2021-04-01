from django.urls import reverse_lazy

from apps.films.forms import *


class BaseFilmMixin:
    template_name = 'films/films_form.html'
    context_object_name = 'object'


class DeletionFilmMixin:
    template_name = 'films/films_confirm_delete.html'
    success_url = reverse_lazy('film_list_url')


class FilmMixin(BaseFilmMixin):
    model = Film
    form_class = FilmForm


class FilmPersonMixin(BaseFilmMixin):
    model = FilmCrewman
    form_class = CrewmanForm


class FilmGenreMixin(BaseFilmMixin):
    model = FilmGenre
    form_class = GenreForm


class FilmRoleMixin(BaseFilmMixin):
    model = RoleInCrew
    form_class = RoleForm
