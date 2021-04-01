from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView,\
    UpdateView, DetailView, ListView

from apps.films.models import Film
from apps.schedules.models import ScheduleDay
from apps_utils.cinema_utils import get_cinema_films , get_cinema_seances , \
    get_random_posters_to_slider
from apps_utils.hall_utils import get_hall_dict, update_hall
from apps_utils.seance_utils import get_schedule_to_context
from .forms import *


class CinemaList(ListView):
    model = Cinema
    context_object_name = 'cinemas'
    extra_context = {
        'films': Film.objects.all(),
        'films_seances':
            get_schedule_to_context(ScheduleDay.get_today_schedule_obj()),
        # 'poster_images': get_random_posters_to_slider(Film.objects.all())
    }


class CinemaDetail(DetailView):
    model = Cinema

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        films = get_cinema_films(self.object),
        context.update({
            'films': films,
            'films_seances':get_schedule_to_context(
                seances=get_cinema_seances(self.object, today=True)),
            # 'poster_images': get_random_posters_to_slider(films)
        })
        return context


class CinemaHallsDetail(DetailView):
    model = Cinema
    template_name = 'cinema/cinema_hall_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'halls': Hall.objects.filter(cinema=self.object)})
        return context


class CinemaCreate(CreateView):
    model = Cinema
    form_class = CinemaForm


class CinemaUpdate(UpdateView):
    model = Cinema
    form_class = CinemaForm


class CinemaDelete(DeleteView):
    model = Cinema
    success_url = reverse_lazy('cinema_list_url')


class DetailHall(View):
    template = 'cinema/hall_detail.html'

    def get(self, request, pk):
        hall_obj = Hall.objects.get(pk=pk)

        if request.is_ajax():
            return JsonResponse({'hall': get_hall_dict(hall_obj)})

        return render(request, self.template, context={
                'slug': pk,
                'hall': hall_obj,
                'halls': Hall.objects.filter(cinema=hall_obj.cinema),
            }
        )


class CreateHall(CreateView):
    model = Hall
    form_class = HallForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'cinema': Cinema.objects.get(id=self.kwargs.get('pk'))
        })
        return context

    def form_valid(self , form):
        obj = form.save(commit=False)
        obj.cinema = Cinema.objects.get(id=self.kwargs.get('pk'))
        self.object = obj.save()
        return super().form_valid(form)


class UpdateHall(View):

    def post(self, request, pk):
        hall = Hall.objects.get(id=pk)
        update_hall(hall, request.POST)
        return HttpResponseRedirect(hall.get_absolute_url())


class DeleteHall(DeleteView):

    model = Hall

    def get_success_url(self):
        return self.object.cinema.get_absolute_url()


class CopyHall(CreateView):

    form_class = HallCopyForm
    template_name = 'cinema/hall_copy.html'

    def form_valid(self, form):
        obj = Hall.objects.get(id=self.kwargs.get('pk'))
        hall_copy = deepcopy(obj)
        hall_copy.cinema = form.cleaned_data['cinema']
        hall_copy.number = form.cleaned_data['number']
        hall_copy.save()
        return HttpResponseRedirect(hall_copy.get_absolute_url())
