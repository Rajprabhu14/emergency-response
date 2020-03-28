from django.shortcuts import render
from rest_framework.exceptions import NotFound

# Create your views here.


def resposne_404(request, *args):
    raise NotFound("Error 404, Page not found", code=404)
