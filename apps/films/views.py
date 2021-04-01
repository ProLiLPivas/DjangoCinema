from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.films.mixins import FilmMixin, FilmPersonMixin, FilmGenreMixin, DeletionFilmMixin, FilmRoleMixin
from .models import *

''' 
        ________________
       /  #############|   _____   ______                                 
       |  #############| /  ###|  /  ###|                          
       |  ### _________/ |  ###|  |  ###|        ______    ___    ___         
       |  ###            |_____/  |  ###|       /  ####\__/###\__/####\                   
       |  #######|        ______  |  ###|       |  ####################\                          
       |  #######|       /  ###|  |  ###|       |  ############# ######|                       
       |  ### ___/       |  ###|  |  ###|       |  ##/   \  ##/   \  ##|                                     
       |  ###|           |  ###|  |  ####\      |  ##|   |  ##|   |  ##|                          
       |  ###|           |  ###|  \   #######|  |  ##|   |  ##|   |  ##|                   
       |____/            |_____/   \_________/  |____/   |____/   |____/       
'''

### Films
class FilmsListView(ListView):
    model = Film

class FilmDetail(DetailView):
    model = Film

class CreateFilm(FilmMixin, CreateView):
    """ """

class UpdateFilm(FilmMixin, UpdateView):
    """ """

class DeleteFilm(DeletionFilmMixin, FilmMixin, DeleteView):
    """ """


### Persons
class PersonsList(ListView):
    model = FilmCrewman

class PersonDetail(DetailView):
    model = FilmCrewman

class CreatePerson(FilmPersonMixin, CreateView):
    """ """

class UpdatePerson(FilmPersonMixin, UpdateView):
    """ """

class DeletePerson(DeletionFilmMixin, FilmPersonMixin, DeleteView):
    """ """


# Genre
class GenreListView(ListView):
    model = FilmGenre

class GenreDetail(DetailView):
    model = FilmGenre

class CreateGenre(FilmGenreMixin, CreateView):
    """ """

class UpdateGenre(FilmGenreMixin, UpdateView):
    """ """

class DeleteGenre(DeletionFilmMixin, FilmGenreMixin, DeleteView):
    """ """


# Role
class RoleListView(ListView):
    model = RoleInCrew

class RoleDetail(DetailView):
    model = RoleInCrew

class CreateRole(FilmRoleMixin, CreateView):
    """ """

class UpdateRole(FilmRoleMixin, UpdateView):
    """ """

class DeleteRole(DeletionFilmMixin, FilmRoleMixin, DeleteView):
    """ """