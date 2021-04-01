from django import forms
from django.core.exceptions import ValidationError

from .models import Seance


class SeanceForm(forms.ModelForm):

    class Meta:
        model = Seance
        fields = ['hall', 'time', 'price_multiplier', 'price']
        widgets = {
            'hall': forms.Select(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control', }),
            'price_multiplier': forms.NumberInput(
                attrs={'type': 'number', 'class': 'form-control'}),
            'price': forms.NumberInput(
                attrs={'type': 'number', 'class': 'form-control'}) ,
        }

    # def clean_time(self):
    #     time = self.changed_data.get('time')
    #     hall = self.changed_data.get('hall')
    #
    #     day = None
    #     film = None
    #     seances_at_same_time = Seance.objects.filter(
    #         film=film,
    #         hall=hall,
    #         day=day,
    #         time__time__range=(time, time + film.time_duration + 10) ,
    #     )
    #
    #     if seances_at_same_time:
    #         raise ValidationError('seance at this time in this hall already exist')
    #     return time
