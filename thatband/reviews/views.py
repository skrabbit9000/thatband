from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Review


class BandListView(ListView):
    model = Review
    template_name = "home.html"
    ordering = ["band_name"]


class BandDetailView(DetailView):
    model = Review
    template_name = "band.html"


class BandAddView(CreateView):
    model = Review
    template_name = "add_band.html"
    fields = ["band_name", "rating", "genre", "description", "sounds_like"]


class BandUpdateView(UpdateView):
    model = Review
    template_name = "update_band.html"
    fields = ["band_name", "rating", "genre", "description", "sounds_like"]

class BandDeleteView(DeleteView):
    model = Review
    template_name = "delete_band.html"
    success_url = reverse_lazy('home')
