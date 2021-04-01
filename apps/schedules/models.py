import datetime
import typing

from django.forms import model_to_dict
from django.db import models
from django.urls import reverse

from apps.films.models import Film
from apps.cinema.models import Hall, Site


class ScheduleDay(models.Model):
    """

    """
    ZERO_DATE = datetime.date(2021, 1, 1)

    date = models.DateField(unique=True, null=True, blank=True)
    slug = models.IntegerField(null=True, blank=True)
    price_multiplier = models.FloatField(default=1.0)

    def get_absolute_url(self):
        return reverse('schedule_day_url', kwargs={'slug': self.slug})

    def gen_slug_by_date(self):
        return (self.date - self.ZERO_DATE).days

    def gen_date_by_slug(self):
        return self.ZERO_DATE + datetime.timedelta(days=self.slug)

    def save(self, *args, **kwargs):
        assert not self.slug or not self.date, \
            'at least one parameter must be specified (slug or date)'
        if not self.slug:
            self.slug = self.gen_slug_by_date()
        if not self.date:
            self.date = self.gen_date_by_slug()
        return super().save(*args, **kwargs)

    @classmethod
    def get_today_schedule_slug(cls) -> int:
        return int((datetime.date.today() - ScheduleDay.ZERO_DATE).days)

    @classmethod
    def get_today_schedule_obj(cls):
        return cls.objects.get_or_create(slug=cls.get_today_schedule_slug())[0]


class Seance(models.Model):
    """

    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    day = models.ForeignKey(ScheduleDay, on_delete=models.CASCADE)
    time = models.TimeField()
    price = models.FloatField(default=100.0)
    price_multiplier = models.FloatField(default=1.0)

    def get_absolute_url(self):
        return reverse('seance_url', kwargs={'seance_id': self.pk})

    def get_delete_url(self):
        return reverse('delete_film_seance_url',
            kwargs={'day_slug': self.day.slug ,'film_id': self.film.pk})

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
            sites = Site.objects.filter(hall=self.hall)
            for site in sites:
                ticket = Ticket(site=site, seance=self)
                ticket.price = self.price_multiplier * self.day.price_multiplier * ticket.price
                ticket.save()
        else:
            super().save(*args, **kwargs)

class Ticket(models.Model):
    """

    """
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)
    is_bought = models.BooleanField(default=False)
    is_reserved = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    def model_to_dict(self):
        ticket_dict = model_to_dict(self)
        ticket_dict.update(model_to_dict(self.site))
        del ticket_dict['seance'], ticket_dict['site'], ticket_dict['hall']
        return ticket_dict