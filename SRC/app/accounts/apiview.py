import requests
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListAPIView, \
    RetrieveDestroyAPIView, ListCreateAPIView

from app.accounts.models import Customer, AddressModel
from app.accounts.serializer import CustomerSerializer, CustomUserSerializer, AddressSerializer


class UserInfo(RetrieveUpdateAPIView):
    # serializer_class = CustomerSerializer
    # lookup_field = request.user
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     return Customer.objects.get(user=user)
    #     # return user.accounts.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return CustomUserSerializer
        return CustomerSerializer

    def get_object(self):
        user = self.request.user
        return Customer.objects.get(user=user)


class AddressInfo(RetrieveUpdateAPIView):
    serializer_class = AddressSerializer
    # queryset = AddressModel.objects.all()

    def get_queryset(self):
        user = self.request.user
        return AddressModel.objects.filter(customer__user__email=user)
        # return user.accounts.all()
    # def get_object(self):
    #     user = self.request.user
    #     customer = Customer.objects.get(user__email=user)
    #     return AddressModel.objects.filter(customer=customer)


class AddressCreate(ListCreateAPIView):
    serializer_class = AddressSerializer


def customer_info_view(request):
    # if request.method == 'POST' and request.is_ajax():
    #     print(dict(request.POST.items()))  # محتویات درخواست مشاهده کنید
    #     input_text = request.POST['inputText']
    #     return JsonResponse({})
    #     print('get',r)
    # if r.status_code == 200:
    #     return HttpResponse(r)
    return render(request,'account/customer_profile.html',{})