from django.urls import path
from .views import BandListView, BandDetailView, BandAddView

urlpatterns = [
    path("", BandListView.as_view(), name="home"),
    path('band/<int:pk>/', BandDetailView.as_view(), name='band'),
    path('band/add', BandAddView.as_view(), name='add_band'),
]
