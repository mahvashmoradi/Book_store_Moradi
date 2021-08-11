from django.http import HttpResponse
from django.shortcuts import render
from app.book.models import BookModel

# Create your views here.
from django.views.generic import ListView


def home(request):
    return render(request, 'pages/home.html')


class HomeView(ListView):
    template_name = 'pages/home.html'
    model = BookModel