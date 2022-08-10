from django.contrib import admin
from .models import User, Movie, Like


admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Like)