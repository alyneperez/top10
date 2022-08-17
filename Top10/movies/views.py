from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import User, Movie, Like


class IndexView(TemplateView):
    template_name = "movies/index.html"


# TODO:
# fixtures dos filmes
# views retornando json
# padrao url

# https://dev.to/brian101co/how-to-return-a-json-response-in-django-gen


def get_movies(request):
    movies = Movie.objects.all()
    data = serialize(
        "json",
        movies,
        fields=("name", "original_name", "director", "genre", "year", "description"),
    )
    return HttpResponse(data, content_type="application/json")

# http://127.0.0.1:8000/movies/allmovies/