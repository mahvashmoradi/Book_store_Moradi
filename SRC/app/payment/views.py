from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
# from rest_framework.generics import get_object_or_404
from django.contrib import messages
from .models import Coupons, Discount
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from app.book.models import BookModel
from .models import Invoice, InvoiceLine
from app.accounts.models import Customer, CityModel, ProvinceModel, AddressModel
from django.contrib.auth.mixins import LoginRequiredMixin
from app.accounts.Mixin import GroupRequiredMixin
from ..accounts.forms import AddressForm


class Cart(View):
    """
    نمایش جزییات سبد خرید: سفارش مشتری را پیدا میکند و محتوای آن را برمیگرداند
    """
    def get(self, request):
        # def cart_detail(request):
        try:
            customer = request.user.customer
            # print(customer)
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)
            # print(customer)
        # print(customer)

        order, created = Invoice.objects.get_or_create(customer=customer, status='O')
        # form = CartAddProductionForm()
        context = {'order': order}
        return render(request, 'payment/detail_cart.html', context)

    def post(self, request):
        """
        کد تخفیف را دریافت کرده و در صورت درست بودن آن را اعمال میکند
        """

        try:
            customer = request.user.customer
            # print(customer)
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)
            # print(customer)
        # print(customer)

        order, created = Invoice.objects.get_or_create(customer=customer, status='O')
        if request.is_ajax():
            # print(dict(request.POST.items()))  # محتویات درخواست مشاهده کنید
            input_code = request.POST['inputText']
            qs_value = Coupons.objects.filter(finished__gte=timezone.now(),
                                              started__lte=timezone.now(), code=input_code)
            total_discount_value = order.total
            if qs_value.exists():
                total_discount_value = order.get_total_discount_price(qs_value[0])
                message = "کد تخفیف اعمال شد "
            else:
                message = "کد اشتباه است یا زمان آن منقضی شده است"
            return JsonResponse({
                'message': message,
                'total_discount_value': total_discount_value
            })


def remove_from_cart(request, pk):
    """
    پاک کردن یک ردیف از سبد خرید
    """

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
    return redirect('payment:cart')


class SelectAddressView(LoginRequiredMixin, View):
    """
    وقتی مشتری برای عملیات پرداخت اقدام کرد، آدرس های قبلی او را به صورت radio_button به او نمایش می دهد، همچنین
    میتواند در همان جا آدرس اضافه کند
    """
    def get(self, request):
        address_form = AddressForm
        customer = request.user.customer
        address_info = AddressModel.objects.filter(customer__user__email=customer)
        return render(request, 'payment/select_address.html',
                      {'address_form': address_form, 'address_info': address_info})

    def post(self, request, *args, **kwargs):

        p_form = AddressForm
        if 'province' in request.POST:
            """
            فرم ایجاد آدرس post شده است. محتویات آن دریافت می شود و در دیتابیس ذخیره می شود
            """
            print(dict(request.POST.items()))

            city_name = request.POST['city']
            province_name = request.POST['province']
            city, created = CityModel.objects.get_or_create(name=city_name)
            province, created = ProvinceModel.objects.get_or_create(name=province_name)
            customer = Customer.objects.get(user=request.user)

            obj_address = AddressModel(customer=customer, province=province,
                                       city=city, address=request.POST['address'],
                                       postal_code=int(request.POST['postal_code']),
                                       phone_number=int(request.POST['phone_number']),
                                       )
            obj_address.save()

            return redirect('./')
        else:
            """
            آدرس مورد نظر مشتری انتخاب شده،
             و آی دی آن ارسال شده است. این آدرس به سفارش مربوطه منتسب می شود
            """
            customer = request.user.customer
            order = Invoice.objects.get(customer=customer, status='O')
            ger_addr = AddressModel.objects.get(id=int(request.POST['flexRadioDefault']))
            order.address = ger_addr
            order.save()
            print(dict(request.POST.items()))
            return redirect('payment:check-out')


class CheckOut(LoginRequiredMixin, View):
    """
    موجودی انبار را جک میکند و پیام میدهد و در صورت نبود مشکل هدایت میکند
    """
    # def test_func(self):  # new
    #     obj = self.get_object()
    #     return obj.customer == self.request.user

    def get(self, request):
        # customer = request.user.customer
        # try:
        customer = request.user.customer
        # except:
        #     device = request.COOKIES['device']
        #     customer = Customer.objects.get(device=device)
        order = Invoice.objects.get(customer=customer, status='O')
        order_item = InvoiceLine.objects.filter(invoice=order)
        isOk = True
        for item in order_item:
            product_quantity = BookModel.objects.filter(id=item.items.id).values('inventory')
            if item.quantity > product_quantity[0]['inventory']:
                messages.error(request,
                               f"  متاسفیم. درخواستی شما از محصول {item.items.name} بیشتر از موجودی انبار است")
                isOk = False
        if isOk:
            order.invoice_complete_date = timezone.now()
            order.status = 'C'
            order.save()
            return render(request, 'payment/finish.html')
        else:
            return redirect('payment:cart')


class DiscountView(GroupRequiredMixin, ListView):
    """
    مشاهده لیست تخفیف محصولات (دسترسی با گروه کارمند و ادمین)
    """

    model = Discount
    # queryset = Task.objects.all()
    template_name = 'payment/discount/discount_list.html'
    group_required = [u'staff_group', u'admin_group']


class CouponsView(GroupRequiredMixin, ListView):
    """
    مشاهده لیست کدهای تخفیف (دسترسی با گروه کارمند و ادمین)
    """
    model = Coupons
    # queryset = Task.objects.all()
    template_name = 'payment/coupons/coupons_list.html'
    group_required = [u'staff_group', u'admin_group']


class DiscountUpdateView(GroupRequiredMixin, UpdateView):
    """
    ویرایش تخفیف های محصولات (دسترسی با گروه کارمند و ادمین)
    """

    model = Discount
    # fields = ('title', 'description',)
    fields = '__all__'
    template_name = 'payment/discount/discount_edit.html'
    success_url = reverse_lazy('payment:discount_list')
    group_required = [u'staff_group', u'admin_group']


class CouponsUpdateView(GroupRequiredMixin, UpdateView):
    """
    ویرایش کدهای تخفیف  (دسترسی با گروه کارمند و ادمین)
    """

    model = Coupons
    # fields = ('title', 'description',)
    fields = '__all__'
    template_name = 'payment/coupons/coupons_edit.html'
    success_url = reverse_lazy('payment:coupons_list')
    group_required = [u'staff_group', u'admin_group']


class CouponsDeleteView(GroupRequiredMixin, DeleteView):
    """
    پاک کردن تخفیف محصولات (دسترسی با گروه کارمند و ادمین)
    """

    model = Coupons
    template_name = 'payment/coupons/coupons_delete.html'
    success_url = reverse_lazy('payment:coupons_list')
    group_required = [u'staff_group', u'admin_group']


class DiscountDeleteView(GroupRequiredMixin, DeleteView):
    """
    پاک کردن کدهای تخفیف (دسترسی با گروه کارمند و ادمین)
    """
    model = Discount
    template_name = 'payment/discount/discount_delete.html'
    success_url = reverse_lazy('payment:discount_list')
    group_required = [u'staff_group', u'admin_group']


class AddDiscountView(GroupRequiredMixin, CreateView):
    """
    افزودن محصول تخفیف خورده (دسترسی با گروه کارمند و ادمین)
    """
    # form_class = BookForm
    model = Discount
    fields = '__all__'
    success_url = reverse_lazy('payment:discount_list')
    template_name = 'payment/discount/discount_add.html'
    group_required = [u'staff_group', u'admin_group']


class AddCouponsView(GroupRequiredMixin, CreateView):
    """
    افزودن کد تخفیف (دسترسی با گروه کارمند و ادمین)
    """
    # form_class = BookForm
    model = Coupons
    fields = '__all__'
    success_url = reverse_lazy('payment:coupons_list')
    template_name = 'payment/coupons/coupons_add.html'
    group_required = [u'staff_group', u'admin_group']


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

