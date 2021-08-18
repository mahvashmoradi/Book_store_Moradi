from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import BookModel, CategoryModel


# Create your views here.
class HomeView(ListView):
    template_name = 'pages/home.html'
    model = BookModel