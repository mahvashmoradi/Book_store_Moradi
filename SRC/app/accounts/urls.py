from django.urls import path
from .views import *
from .apiview import UserInfo, AddressInfo, customer_info_view

app_name = 'app.accounts'

urlpatterns = [
    # path('', home),
    path('sign-up/', CustomerSignUp.as_view(), name='customer-sign-up'),
    path('staff-sign-up/', StaffSignUp.as_view(), name='staff-sign-up'),
    path('edit-user/<int:pk>/', CustomerUpdateView.as_view(), name='edit-user'),
    path('complete-info/', CustomerInfoView.as_view(), name='complete-info'),
    path('address-delete/<int:id>/', delete_address, name='delete-address'),
    path('address-edit/<int:id>/', EditAddress.as_view(), name='edit-address'),
    path('staff/', StaffView.as_view(), name='staff_menu'),
    #api
    path('complete-view-api-info/', customer_info_view, name='complete-view-api-info'),
    path('complete-api-info/', UserInfo.as_view(), name='complete-api-info'),
    path('address-info/', AddressInfo.as_view(), name='address-info'),

]
