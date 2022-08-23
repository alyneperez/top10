from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=6, verbose_name=_("Password"))
    photo = models.ImageField(verbose_name=_("Photo"))
    movies = models.ManyToManyField("Movie", through="Like")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    original_name = models.CharField(max_length=50, verbose_name=_("Original name"))
    director = models.CharField(max_length=30, verbose_name=_("Director"))
    genre = models.CharField(max_length=10, verbose_name=_("Genre"))
    year = models.IntegerField(verbose_name=_("Year"))
    description = models.CharField(max_length=500, verbose_name=_("Description"))
    photo = models.ImageField(default="", verbose_name=_("Photo"))

    def __str__(self):
        return f"{self.name},{self.original_name},{self.director},{self.year}."

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")


class Like(models.Model):
    like = models.IntegerField(verbose_name=_("Like"))
    user = models.ForeignKey("User", on_delete=models.PROTECT, verbose_name=_("User"))
    movie = models.ForeignKey(
        "Movie", on_delete=models.PROTECT, verbose_name=_("Movie")
    )

    def __str__(self):
        return f"{self.movie}"

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
