from django.urls import path
from .views import home, InvoiceView
urlpatterns = [
    path('', home),
    path('Invoice/', InvoiceView.as_view()),

    ]