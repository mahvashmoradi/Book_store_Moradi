from django import forms

PRODUCT_CHOISE_QUANTITY = [(i, str(i)) for i in range(1, 21)]


class CartAddProductionForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_CHOISE_QUANTITY, coerce=int)
    quantity = forms.IntegerField(initial=1)
    # override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
