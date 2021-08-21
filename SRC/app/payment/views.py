from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import View
from rest_framework.generics import get_object_or_404

from .models import Invoice
# Create your views here.
from django.views.generic import ListView
from app.book.models import BookModel
from .models import Invoice, InvoiceLine
from app.accounts.models import Customer


# def add_to_cart(request, pk):
#     item = get_object_or_404(BookModel, pk=pk)
#     if request.user.is_authenticated:
#         client = get_object_or_404(Customer, user__email=request.user)
#         order_get, created = Invoice.objects.get_or_create(customer=client, status='O')
#         # order_get.customer.add(client)
#         # order_get.save()
#         # order_item, created = InvoiceLine.objects.get_or_create(invoice= order )
#         # order_qs = InvoiceLine.objects.filter(costomer=request.user, status='O')
#         order_item_qs = InvoiceLine.objects.filter(invoice=order_get.id)
#         if order_item_qs.exists():
#             order = order_item_qs[0]
#             # check if the order item is in the order
#             if order_item_qs.items.filter(items__id=item.pk).exists():
#                 order_item_qs.quantity += 1
#                 order_item_qs.save()
#                 # messages.info(request, "This item quantity was updated.")
#                 return redirect("pages:home")
#             else:
#                 InvoiceLine.objects.create(invoice=order, quantity=1,
#                                                                  unit_price=item.price, items=item)
#                 # order.items.add(order_item)
#                 # # messages.info(request, "This item was added to your cart.")
#                 # return redirect("pages:home")
#                 order_get.invoice_date = timezone.now()
#                 order_get.save()
#                 # order_datail = InvoiceLine.objects.create(
#                 #     items=item, quantity= 1, unit_price= item.price_discount)
#                 # order_datail.invoice.add(orderid)
#                 # messages.info(request, "This item was added to your cart.")
#     return redirect("pages:home")

def cart_detail(request):
    print('request', request)
    try:
        customer = request.user.customer
        print(customer)

    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        print(customer)
    print(customer)

    order, created = Invoice.objects.get_or_create(customer=customer, status= 'O')
    # form = CartAddProductionForm()
    context = {'order': order}
    return render(request, 'payment/detail_cart.html', context)


def remove_from_cart(request, pk):
    product = BookModel.objects.get(id=pk)
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
    order, created = Invoice.objects.get_or_create(customer=customer, status='O')
    order_item, created = InvoiceLine.objects.get_or_create(invoice=order, items=product)
    order.Items.remove(order_item)
    order_item.delete()
    # return reverse("app.payment:cart")
    return redirect('payment:cart')

# def remove_from_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 user=request.user,
#                 ordered=False
#             )[0]
#             order.items.remove(order_item)
#             order_item.delete()
#             messages.info(request, "This item was removed from your cart.")
#             return redirect("core:order-summary")
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("core:product", slug=slug)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("core:product", slug=slug)
