from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

from allauth.account.views import SignupView
from django.views import View

from .forms import StaffSignupForm, CustomerSignupForm


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
    template_name = 'account/allauth/customer_signup.html'
    form_class = CustomerSignupForm
    # redirect_field_name = 'next'
    view_name = 'customer-sign-up'

    def get_context_data(self, **kwargs):
        ret = super(CustomerSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


class StaffSignUp(SignupView):
    template_name = 'account/allauth/staff-sing-up.html'
    form_class = StaffSignupForm
    # redirect_field_name = 'next'
    view_name = 'staff-sign-up'

    def get_context_data(self, **kwargs):
        ret = super(StaffSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


class StaffView(View):

    def get(self, request):
        return render(request, 'book/staff.html')
