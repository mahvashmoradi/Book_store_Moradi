from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Invoice
# Create your views here.
from django.views.generic import ListView


def home(request):
    return HttpResponse('hi')


class InvoiceView(ListView):
    # def get(self, request):
    #
    #     return render(request, 'payment/Invoice.html')
    model = Invoice
    template_name = 'payment/Invoice.html'
