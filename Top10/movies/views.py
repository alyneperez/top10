from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import User, Movie, Like


class IndexView(TemplateView):
    template_name = "movies/index.html"


# GET ALL MOVIES
def get_movies(request):
    movies = Movie.objects.all()
    data = serialize(
        "json",
        movies,
        fields=("name", "original_name", "director", "genre", "year", "description"),
    )
    return HttpResponse(data, content_type="application/json")


# GET ONE MOVIE
def get_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return HttpResponse("Error: 404 - Movie not found")
    data = serialize(
        "json",
        [movie],
        fields=("name", "original_name", "director", "genre", "year", "description"),
    )
    return HttpResponse(data, content_type="application/json")


# GET ALL USERS
def get_users(request):
    users = User.objects.all()
    data = serialize(
        "json",
        users,
        fields=("name", "email"),
    )
    return HttpResponse(data, content_type="application/json")


# GET ONE USER
def get_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse("Error: 404 - User not found")
    data = serialize(
        "json",
        [user],
        fields=("name", "original_name", "director", "genre", "year", "description"),
    )
    return HttpResponse(data, content_type="application/json")


# GET USER TOP10 MOVIES
# def get_user_top_10(request, id):
#     try:
#         likes = Like.objects.all(id=id)[:10]
#     except Like.DoesNotExist:
#         return HttpResponse("Error: 404 - Top10 not found")
#     print(request)
#     print(likes)
#     data = serialize(
#         "json",
#         [likes],
#         fields=("movie"),
#     )
#     return HttpResponse(data, content_type="application/json")


# ToDo
# def get_user_top_10(request, id):
#     likes = Like.objects.all(user_id=id) >> revisar lógica

# def like_dislike(request, user_id, movie_id):
# like = Like.objects.get(user_id=user_id,movie_id=movie_id)

# URL likes (VERIFICAR QTS LIKES=10MAX)
# URL deslikes
