from django import forms

PRODUCT_CHOICE_QUANTITY = [(i, str(i)) for i in range(1, 21)]


class CartAddProductionForm(forms.Form):
    """
    انتخاب تعداد محصولات
    """
    # quantity = forms.TypedChoiceField(choices=PRODUCT_CHOICE_QUANTITY, coerce=int)
    quantity = forms.IntegerField(initial=1 , label='تعداد')

    # override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    def clean(self):
        super(CartAddProductionForm, self).clean()
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1:
            # self.cleaned_data['quantity'] = 1
            self._errors['quantity'] = self.error_class([
                'درخواست نمیتواند کمتر از یک باشد'])
        return self.cleaned_data
# class SelectAddressForm(forms.Form):
#     # quantity = forms.TypedChoiceField(choices=PRODUCT_CHOISE_QUANTITY, coerce=int)
#     customer = request.user.customer
#     # user_info = Customer.objects.get(user__email=customer)
#     address_info = AddressModel.objects.filter(customer__user__email=customer)
#
#     select_address = forms.ModelChoiceField(queryset=address_info)
# override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
