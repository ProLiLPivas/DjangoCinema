from django import forms

from apps.films.models import *


class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'poster': forms.FileInput(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
            'time_duration': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
            'is_showing': forms.CheckboxInput(attrs={}),
        }


class RoleForm(forms.ModelForm):

    class Meta:
        model = RoleInCrew
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
        }


class CrewmanForm(forms.ModelForm):

    class Meta:
        model = FilmCrewman
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'day_birth': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
            'day_death': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', }),
            'biography': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
            'role_in_crew': forms.Select(
                attrs={'class': 'form-control'}),
        }


class GenreForm(forms.ModelForm):

    class Meta:
        model = FilmGenre
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
        }