from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from rest_framework.generics import get_object_or_404

from .models import Invoice
# Create your views here.
from django.views.generic import ListView
from app.book.models import BookModel
from .models import Invoice, InvoiceLine
from app.accounts.models import Customer
def home(request):
    return HttpResponse('hi')


class InvoiceView(ListView):
    # def get(self, request):
    #
    #     return render(request, 'payment/Invoice.html')
    model = Invoice
    template_name = 'payment/Invoice.html'


def add_to_cart(request, pk):
    item = get_object_or_404(BookModel, pk=pk)
    client = get_object_or_404(Customer, user__email=request.user)
    orderid, created = Invoice.objects.get_or_create(
        customer=client,
        status='O'
    )
    # order_item, created = InvoiceLine.objects.get_or_create(
    #     invoice= orderid
    # )

    # order_qs = InvoiceLine.objects.filter(costomer=request.user, status='O')
    order_qs = InvoiceLine.objects.filter(invoice= orderid)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order_qs.items.filter(items__id=item.pk).exists():
            order_qs.quantity += 1
            order_qs.save()
            # messages.info(request, "This item quantity was updated.")
            return redirect("pages:home")
        # else:
            # order.items.add(order_item)
            # # messages.info(request, "This item was added to your cart.")
            # return redirect("pages:home")
        else:
            orderid_invoice_date = timezone.now()
            orderid.save()
            order_datail = InvoiceLine.objects.create(
                items=item, quantity= 1, unit_price= item.price_discount)
            order_datail.invoice.add(orderid)
            # messages.info(request, "This item was added to your cart.")
            return redirect("pages:home")
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