from django.urls import path
from .views import *
from rest_framework import routers
from .apiview import InvoiceApiView, CreateOrder, AddOrder
app_name = 'app.payment'

router = routers.DefaultRouter()
router.register('invoice', InvoiceApiView, basename='invoice')

urlpatterns = [
    # path('', home),
    # path('Invoice/', InvoiceView.as_view()),
    # path('add_cart/<int:pk>', add_to_cart, name ='add_to_cart'),
    path('remove/<int:pk>', remove_from_cart, name ='remove_from_cart'),
    path('cart_detail/', Cart.as_view(), name ='cart'),
    path('check-out/', CheckOut.as_view(), name ='check-out'),
    path('order/',CreateOrder.as_view(), name ='add_to_cart_api'),
    path('addorder/',AddOrder.as_view(), name ='add_to_o_api'),
    path('coupons/', CouponsView.as_view(), name='coupons_list'),
    path('coupons-edit/<int:pk>/', CouponsUpdateView.as_view(), name='coupons_edit'),
    path('coupons-delete/<int:pk>/', CouponsDeleteView.as_view(), name='coupons_delete'),
    path('add-coupons/', AddCouponsView.as_view(), name='add_coupons'),
    path('discount/', DiscountView.as_view(), name='discount_list'),
    path('discount-edit/<int:pk>/', DiscountUpdateView.as_view(), name='discount_edit'),
    path('discount-delete/<int:pk>/', DiscountDeleteView.as_view(), name='discount_delete'),
    path('add-discount/', AddDiscountView.as_view(), name='add_discount'),

    ]

urlpatterns += router.urls
