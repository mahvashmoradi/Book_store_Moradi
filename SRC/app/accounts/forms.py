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
from django import forms
from django.contrib.auth.models import Group


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
        group = Group.objects.get(name='staff_group')
        # group.user_set.add(customer)
        # group.save()
        user.groups.add(group)
        user.save()
        # Add your own processing here.
        # You must return the original result.
        return user


# customer = Customer.objects.get(user=request.user)
# choices = [(address.id, address.address) for address in AddressModel.objects.filter(customer=customer )]
class AddressForm(forms.Form):
    """
    فرم آدرس
    """
    # def __init__(self, *args, **kwargs):
    #     super(AddressForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
    province = forms.CharField(label='استان',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(label='شهر',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='آدرس',max_length=100,widget=forms.Textarea(attrs={'class':'form-control'}))
    postal_code = forms.CharField(label='کد پستی',max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label='شماره تلفن', max_length=11,widget=forms.TextInput(attrs={'class':'form-control'}))
    # choices= forms.ChoiceField(label='آدرس منتخب',choices=choices)
    #
    # def clean_title(self):
    #     super(TaskForm, self).clean()
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 5:
    #         self._errors['title'] = self.error_class([
    #             'اینم فارسی که خیالت راحت شه'])

    # def clean(self):
    #     # data from the form is fetched using super function
    #     super(TaskForm, self).clean()
    #
    #     # extract the title and text field from the data
    #     title = self.cleaned_data.get('title')
    #     description = self.cleaned_data.get('description')
    #
    #     # # conditions to be met for the title length
    #     # if len(title) < 5:
    #     #     self._errors['title'] = self.error_class([
    #     #         'Minimum 5 characters required'])
    #     if len(description) < 10:
    #         self._errors['description'] = self.error_class([
    #             'Post Should Contain a minimum of 10 characters'])
    #
    #     # return any errors if found
    #     return self.cleaned_data
