from copy import copy, deepcopy

from django.db import models
from django.urls import reverse


class Cinema(models.Model):
    """

    """
    title = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('cinema_url', kwargs={'pk': self.pk})

    def get_create_url(self):
        return reverse('hall_create_url', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('cinema_update_url' , kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('cinema_delete_url' , kwargs={'pk': self.pk})



class Hall(models.Model):
    """

    """
    number = models.IntegerField(default=1)
    sites_amount = models.IntegerField()
    rows_amount = models.IntegerField()
    is_vip = models.BooleanField(default=False)
    cinema = models.ForeignKey(
        'Cinema', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('hall_url', kwargs={'pk': self.pk})

    # def get_delete_url(self):
    #     return reverse('hall_delete_url', kwargs={'pk': self.pk})

    def __str__(self):
        return 'hall: {} cinema: {}'.format(self.number, self.cinema.title)

    def __copy__(self):
        return Hall.objects.create(
            number=self.number,
            sites_amount=self.sites_amount,
            rows_amount=self.rows_amount,
            is_vip=self.is_vip,
            cinema=self.cinema
        )

    def __deepcopy__(self, kwargs):
        hall_copy = copy(self)
        sites = list(Site.objects.filter(hall=hall_copy))
        for site in sites:
            copy(site)
        return hall_copy

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
            self._make_sites_for_new_hall()
        else:
            super().save(*args, **kwargs)

    def _make_sites_for_new_hall(self) -> None:
        """
        when we create new hall we using this func to
        generate site places to it.
        """
        for row in range(self.rows_amount):
            for site in range(self.sites_amount):
                Site.objects.create(
                    hall=self,
                    row=row + 1,
                    site_position=site + 1,
                    site_number=site + 1
                )


class Site(models.Model):
    """

    """
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    row = models.IntegerField()
    # necessary to draw correct hall scheme it html-table
    site_position = models.IntegerField()
    # necessary to show correct site number
    site_number = models.IntegerField()
    is_exist = models.BooleanField(default=True)

    def __copy__(self, hall_obj=None):
        kwarg = {
            'row': self.row,
            'site_position': self.site_position,
            'site_number': self.site_number,
            'is_exist': self.is_exist,
        }
        if not hall_obj:
            kwarg.update({'hall': self.hall})
        else:
            kwarg.update({'hall': hall_obj})
        return Site.objects.create(**kwarg)





