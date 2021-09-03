from django.contrib import messages
from django.shortcuts import render, redirect
from app.accounts.Mixin import GroupRequiredMixin
from allauth.account.views import SignupView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from .forms import StaffSignupForm, CustomerSignupForm, AddressForm
from .models import Customer, AddressModel, CityModel, ProvinceModel
from ..payment.models import Invoice


# Create your views here.

# class AccountSignupView(SignupView):
#     # Signup View extended
#
#     # change template's name and path
#     # template_name = "users/custom_signup.html"
#
#     # You can also override some other methods of SignupView
#     # Like below:
#     form_class =
#     # def form_valid(self, form):
#     #     ...
#     #
#     # def get_context_data(self, **kwargs):
#     #     ...


class CustomerSignUp(SignupView):
    """
    ثبت نام مشتریان
    """
    template_name = 'account/allauth/customer_signup.html'
    form_class = CustomerSignupForm
    # redirect_field_name = 'next'
    view_name = 'customer-sign-up'

    def get_context_data(self, **kwargs):
        ret = super(CustomerSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


class StaffSignUp(SignupView):
    """
    ثبت نام کارمندان
    """
    template_name = 'account/allauth/staff-sing-up.html'
    form_class = StaffSignupForm
    # redirect_field_name = 'next'
    view_name = 'staff-sign-up'

    def get_context_data(self, **kwargs):
        ret = super(StaffSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


class StaffView(GroupRequiredMixin, View):
    """
    لیست کارهایی که کارمند میتواند انجام دهد
    """
    group_required = [u'staff_group', u'admin_group']

    def get(self, request):
        return render(request, 'book/staff.html')


class CustomerInfoView(View):
    """
    پروفایل مشتریان
    """
    def get(self, request):
        form = AddressForm
        customer = request.user.customer
        user_info = Customer.objects.get(user__email=customer)
        address_info = AddressModel.objects.filter(customer__user__email=customer)
        order = Invoice.objects.filter(customer=customer)
        return render(request, 'account/customer_menu.html', {'user_info': user_info,
                                                              'address': address_info,
                                                              'history': order,
                                                              'form': form})

    def post(self, request, *args, **kwargs):
        """
        ذخیره آدرس جدید برای مشتری
        """
        form = AddressForm(request.POST or None)
        if form.is_valid():
            city_name = request.POST['city']
            province_name = request.POST['province']
            city, created = CityModel.objects.get_or_create(name=city_name)
            province, created = ProvinceModel.objects.get_or_create(name=province_name)
            customer = Customer.objects.get(user=request.user)

            obj_address = AddressModel(customer=customer, province=province,
                                       city=city, address=request.POST['address'],
                                       postal_code=request.POST['postal_code'],
                                       phone_number=request.POST['phone_number'],
                                       )
            obj_address.save()
            return redirect('./')


def delete_address(request, id):
    """
    حذف کردن آدرس ها(اگر فقط یک آدرس باشد، اجازه حذف نمی دهد)
    """
    customer = Customer.objects.get(user=request.user)
    addr = AddressModel.objects.filter(customer=customer)
    if len(addr) > 1:
        AddressModel.objects.filter(id=id).delete()
    else:
        messages.error(request, 'یک آدرس باید در حساب کاربری شما موجود باشد')
    return redirect('accounts:complete-info')


class EditAddress(View):
    """
    ویرایش آدرس
    """
    def get(self, request, id):
        obj_address = AddressModel.objects.get(id=id)
        form = AddressForm
        return render(request, 'account/address_edit.html', {'form': form})

    def post(self, request, id):
        customer = Customer.objects.get(user=request.user)
        obj_address = AddressModel.objects.get(id=id)
        form = AddressForm(request.POST or None)
        if form.is_valid():
            city_name = request.POST['city']
            province_name = request.POST['province']
            city, created = CityModel.objects.get_or_create(name=city_name)
            province, created = ProvinceModel.objects.get_or_create(name=province_name)

            obj_address.city = city
            obj_address.save()

            obj_address.province = province
            obj_address.save()

            obj_address.address = request.POST['address']
            obj_address.save()

            obj_address.phone_number = request.POST['phone_number']
            obj_address.save()

            obj_address.postal_code = request.POST['postal_code']
            obj_address.save()
        return redirect('accounts:complete-info')


class CustomerUpdateView(UpdateView):
    """
    ویرایش پروفایل کاربری
    """
    model = Customer
    # fields = ('title', 'body',)
    fields = ['first_name', 'last_name', 'gender']
    template_name = 'account/user_edit.html'
    success_url = reverse_lazy('accounts:complete-info')
