from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "movies/index.html"

#TO DO:
#fixtures dos filmes
#views retornando json
# padrao url