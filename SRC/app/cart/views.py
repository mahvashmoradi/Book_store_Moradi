from django.shortcuts import render, get_object_or_404, redirect
# from django.views.decorators.http import require_POST

from .cart import Cart
# Create your views here.
from django.views import View
from app.book.models import BookModel
from .forms import CartAddProductionForm


class AddCart(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(BookModel, id=product_id)
        form = CartAddProductionForm(request.POST)
        print(form)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        return redirect('cart:cart_detail')


class RemoveCart(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(BookModel, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


class DetailCart(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductionForm(initial={'quantity':item['quantity'],'override':True})
        # cart_product_form = CartAddProductionForm
        return render(request, 'cart/detail.html', {'cart': cart})
