from django.urls import path
from .views import home, InvoiceView, add_to_cart
from rest_framework import routers
from .apiview import InvoiceApiView, CreateOrder, AddOrder

router = routers.DefaultRouter()
router.register('invoice', InvoiceApiView, basename='invoice')

urlpatterns = [
    path('', home),
    path('Invoice/', InvoiceView.as_view()),
    path('add_cart/<int:pk>', add_to_cart, name ='add_to_cart'),
    path('order/',CreateOrder.as_view(), name ='add_to_cart_api'),
    path('addorder/',AddOrder.as_view(), name ='add_to_o_api'),

    ]

urlpatterns += router.urls
