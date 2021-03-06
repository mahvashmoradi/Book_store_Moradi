from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListAPIView, \
    RetrieveDestroyAPIView, ListCreateAPIView

from app.accounts.models import Customer, AddressModel
from app.accounts.serializer import CustomerSerializer, CustomUserSerializer, AddressSerializer
from app.payment.models import Invoice, InvoiceLine


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

    # def get_object(self):
    #     user = self.request.user
    #     customer = Customer.objects.get(user__email=user)
    #     return AddressModel.objects.filter(customer=customer)


class AddressCreate(ListCreateAPIView):
    serializer_class = AddressSerializer

@login_required()
def customer_info_view(request):
    # if request.method == 'POST' and request.is_ajax():
    #     print(dict(request.POST.items()))  # محتویات درخواست مشاهده کنید
    #     input_text = request.POST['inputText']
    #     return JsonResponse({})
    #     print('get',r)
    # if r.status_code == 200:
    #     return HttpResponse(r)
    customer = request.user.customer
    user_info = Customer.objects.get(user__email=customer)
    address_info = AddressModel.objects.filter(customer__user__email=customer)
    # order = Invoice.objects.filter(customer=customer)
    return render(request, 'account/customer_profile.html', {'user_info': user_info,
                                                             'address': address_info})
