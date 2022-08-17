from django.urls import path
from .views import IndexView, get_movies


urlpatterns = [
    path(" ", IndexView.as_view(), name="index"),
    path("allmovies/", get_movies, name="get_movies")
]