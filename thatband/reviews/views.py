from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
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
    fields = ['band_name', 'rating', 'genre', 'description', 'sounds_like'] 
