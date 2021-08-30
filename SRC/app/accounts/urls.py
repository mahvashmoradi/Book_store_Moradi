from django.urls import path
from .views import *
from .apiview import *

app_name = 'app.accounts'

urlpatterns = [
    # path('', home),
    path('sign-up/', CustomerSignUp.as_view(), name='customer-sign-up'),
    path('staff-sign-up/', StaffSignUp.as_view(), name='staff-sign-up'),
    #api

    path('complete-info/', customer_info_view, name='complete-info'),
    path('complete-api-info/', UserInfo.as_view(), name='complete-api-info'),
    path('address-info/', AddressInfo.as_view(), name='address-info'),
    path('staff/', StaffView.as_view(), name='staff_menu'),

]
