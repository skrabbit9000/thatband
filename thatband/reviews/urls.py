from django.urls import path
from .views import (
    BandListView,
    BandDetailView,
    BandAddView,
    BandUpdateView,
    BandDeleteView,
)

urlpatterns = [
    path("", BandListView.as_view(), name="home"),
    path("band/<int:pk>/", BandDetailView.as_view(), name="band"),
    path("band/add/", BandAddView.as_view(), name="add_band"),
    path("band/<int:pk>/update/", BandUpdateView.as_view(), name="update_band"),
    path("band/<int:pk>/delete/", BandDeleteView.as_view(), name="delete_band"),
]
