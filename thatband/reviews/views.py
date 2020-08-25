from django.views import generic
from .models import Review


class BandListView(generic.ListView):
    model = Review
    template_name = "home.html"
