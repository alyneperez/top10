from django.urls import path
from .views import IndexView, get_movies, get_movie, get_users, get_user


urlpatterns = [
    path(" ", IndexView.as_view(), name="index"),

    path("allmovies/", get_movies, name="get_movies"),
    path("movie/<int:id>", get_movie, name="get_movie"),

    path("allusers/", get_users, name="get_users"),
    path("user/<int:id>", get_user, name="get_user"),

    # path("top10/<int:id>", get_user_top_10, name="get_user_top_10"),
]
# http://127.0.0.1:8000/movies/allmovies/
# http://127.0.0.1:8000/movie/<id>/

# http://127.0.0.1:8000/movies/allusers/
#  http://127.0.0.1:8000/movies/user/<id>

#  http://127.0.0.1:8000/movies/top10/<id>