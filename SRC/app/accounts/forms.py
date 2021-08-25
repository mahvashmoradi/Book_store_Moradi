# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
#
#
# class StaffSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_staff = True
#         if commit:
#             user.save()
#         return user

# ACCOUNT_SIGNUP_FORM_CLASS (=None)
from allauth.account.forms import SignupForm

from app.accounts.models import Customer


class CustomerSignupForm(SignupForm):

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomerSignupForm, self).save(request)
        user.save()
        # Add your own processing here.

        # You must return the original result.
        return user


class StaffSignupForm(SignupForm):

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(StaffSignupForm, self).save(request)
        user.is_staff = True
        user.save()
        # Add your own processing here.
        # You must return the original result.
        return user
