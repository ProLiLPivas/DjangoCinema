from django import forms

from .models import *


class CinemaForm(forms.ModelForm):

    class Meta:
        model = Cinema
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['number', 'sites_amount', 'rows_amount', 'is_vip']

        widgets = {
            'number': forms.NumberInput(
                attrs={'class': 'form-control', 'id': 'new-hall-name'}),
            'sites_amount': forms.TextInput(
                attrs={'class': ' col', 'v-model': 'sites_amount'}),
            'rows_amount': forms.TextInput(
                attrs={'class': ' col', 'v-model': 'rows_amount'}),
            'is_vip': forms.CheckboxInput(attrs={'class': 'col'}),
            'cinema': forms.Select(attrs={'class': 'form-control'})
        }


class HallCopyForm(forms.ModelForm):
    class Meta:

        model = Hall
        fields = ['number', 'cinema']

        widgets = {
            'number': forms.NumberInput(
                attrs={'class': 'form-control', 'id': 'new-hall-name'}),
            'cinema': forms.Select(attrs={'class': 'form-control'})
        }