from django.db import models
from django.urls import reverse


class Film(models.Model):
    """

    """
    class_name = 'Film'

    name = models.CharField(max_length=100)
    poster = models.ImageField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    time_duration = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_showing = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('about_film_url' , kwargs={'pk': self.pk})

    def get_add_seance_url(self , day_slug):
        kwargs = {'day_slug': day_slug, 'film_id': self.pk}
        return reverse('add_seance_url', kwargs=kwargs)



    def __str__(self):
        return self.name


class RoleInCrew(models.Model):
    """

    """
    class_name = 'Role'

    type = models.CharField(max_length=50)
    description = models.TextField(null=True , blank=True)

    def get_absolute_url(self):
        return reverse('about_role_url', kwargs={'pk': self.pk})



    def __str__(self):
        return self.type


class FilmCrewman(models.Model):
    class_name = 'Person'

    name = models.CharField(max_length=100)
    day_birth = models.DateField(null=True, blank=True)
    day_death = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    role_in_crew = models.ForeignKey(
        RoleInCrew, on_delete=models.DO_NOTHING, null=True, blank=True)

    # films = models.ManyToManyField('Film', related_name='films', blank=True)

    def get_absolute_url(self):
        return reverse('about_person_url', kwargs={'pk': self.pk})



    def __str__(self):
        return self.name


class FilmGenre(models.Model):
    class_name = 'Genre'

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('about_genre_url', kwargs={'pk': self.pk})




class FilmImages(models.Model):

    image = models.ImageField(null=True, blank=True)
    film = models.ForeignKey(
        'Film', on_delete=models.CASCADE, null=True, blank=True)
