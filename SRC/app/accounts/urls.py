from django.urls import path
from .views import *
app_name = 'app.accounts'

urlpatterns = [
    # path('', home),
    path('sign-up/', CustomerSignUp.as_view(), name='customer-sign-up'),
    path('staff-sign-up/', StaffSignUp.as_view(), name='staff-sign-up'),
    ]
