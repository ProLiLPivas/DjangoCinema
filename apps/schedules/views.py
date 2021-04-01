from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, \
    DetailView, UpdateView, DeleteView

from apps.films.models import Film
from apps.schedules.models import ScheduleDay, Ticket
from apps_utils.seance_utils import get_schedule_to_context
from .forms import *


class ScheduleView(View):

    def get(self, request):
        slug = ScheduleDay.get_today_schedule_slug()
        return redirect(
            reverse_lazy('schedule_day_url', kwargs={'day_slug': slug})
        )


class ScheduleDayDetail(DetailView):

    def get_object(self, queryset=None):
        return ScheduleDay.objects.get_or_create(
            slug=self.kwargs.get('day_slug'))[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'films': Film.objects.all(),
            'films_seances': get_schedule_to_context(self.get_object())
        })
        return context


class AddSeanceView(CreateView):
    model = Seance
    form_class = SeanceForm
    success_url = reverse_lazy('schedule_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'day': ScheduleDay.objects.get(slug=self.kwargs.get('day_slug')),
            'film': Film.objects.get(id=self.kwargs.get('film_id'))
        })
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.day = ScheduleDay.objects.get(slug=self.kwargs.get('day_slug'))
        obj.film = Film.objects.get(id=self.kwargs.get('film_id'))
        self.object = obj.save()

        return super().form_valid(form)


class DeleteFilmSeanceView(DeleteView):

    context_object_name = 'seance'
    template_name = 'schedules/film_seances_confirm_delete.html'
    success_url = reverse_lazy('schedule_url')

    def get_object(self, queryset=None):
        return Seance.objects.filter(
            day__slug=self.kwargs.get('day_slug'),
            film__id=self.kwargs.get('film_id')
        )


class SeanceDetail(View):
    template = 'schedules/seance_detail.html'

    def get(self, request, seance_id):
        seance_obj = Seance.objects.get(pk=seance_id)

        if request.is_ajax():
            seance_dict = SeanceDetail.get_seance_dict(seance_obj)
            return JsonResponse({'seance': seance_dict})

        context = {'slug': seance_id, 'seance': seance_obj,}
        return render(request, self.template, context=context)

    @staticmethod
    def get_seance_dict(seance: Seance) -> dict:
        sites = SeanceDetail.get_tickets_list(seance)
        seance_dict = model_to_dict(seance)
        seance_dict.update({'sites': sites})

        return seance_dict

    @staticmethod
    def get_tickets_list(seance_obj: Seance) -> list:
        tickets = Ticket.objects.filter(seance=seance_obj)
        return [Ticket.model_to_dict(ticket) for ticket in tickets]





class UpdateSeanceView(UpdateView):
    model = Seance
    form_class = SeanceForm
    pk_url_kwarg = 'seance_id'
    success_url = reverse_lazy('schedule_url')

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'day': self.object.day,
            'film': self.object.film,
        })
        return context


class DeleteSeanceView(DeleteView):
    model = Seance
    pk_url_kwarg = 'seance_id'
    success_url = reverse_lazy('schedule_url')




# class BuyTicketView:
#     pass
#
#
# class ReserveTickets:
#     pass