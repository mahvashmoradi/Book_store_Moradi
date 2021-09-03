from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.views import View
from app.accounts.models import Customer
from app.book.models import BookModel, CategoryModel
from app.payment.forms import CartAddProductionForm
from app.payment.models import Invoice, InvoiceLine


# Create your views here.
class HomeView(View):
    """
     اگر id دریافت نکرد، همه محصولات و اگر دریافت کرد محصولات همان دسته را نمایش می دهد
    """
    def get(self, request, id=None):
        product = BookModel.objects.all()
        # for i in product:
        #     i.cal_discount_price()

        categories = CategoryModel.objects.all()
        form = CartAddProductionForm
        category = None
        if id:
            category = get_object_or_404(CategoryModel, id=id)
            product = BookModel.objects.filter(categories=category)
        return render(request, 'pages/home.html',
                      {'product': product, 'categories': categories, 'category': category, 'form': form})

    def post(self, request, id=None):
        """
         عبارت وارد شده در کادر سرچ را دریافت میکند و در دیتابیس سرچ میکند و لیست برمیگرداند
        """
        if request.is_ajax():
            print(dict(request.POST.items()))  # محتویات درخواست مشاهده کنید
            input_text = request.POST['inputText']
            if id:
                category = get_object_or_404(CategoryModel, id=id)
                if input_text:
                    books = BookModel.objects.filter(name__contains=input_text, categories=category)
                else:
                    books = BookModel.objects.filter(categories=category)
            else:
                if input_text:
                    books = BookModel.objects.filter(name__contains=input_text)
                else:
                    books = BookModel.objects.all()
            # message =  str(datetime.now())
            return JsonResponse({
                # 'message':message,
                'books': list(books.values())
            })


class ProductDetailView(View):
    """
    # محصول را نمایش میدهد و همچنین یک فرم برای دریافت میزان درخواستی کالا دارد
    """
    def get(self, request, pk):
        object = get_object_or_404(BookModel, id=pk)
        form = CartAddProductionForm
        return render(request, 'pages/product.html', {'object': object, 'form': form})

    def post(self, request, pk):
        """
         # محصول را دریافت میکند. مشتری را تشخیص داده و در فاکتور و جزییات فاکتور ثبت میکند
        """
        product = BookModel.objects.get(id=pk)
        # Get user account information
        print(request.user)

        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Invoice.objects.get_or_create(customer=customer, status='O')
        orderItem, created = InvoiceLine.objects.get_or_create(invoice=order, items=product)
        orderItem.quantity = request.POST['quantity']
        orderItem.save()
        return redirect('payment:cart')

# class ProductDetailView(DetailView):
#     model = BookModel
#     template_name = 'pages/product.html'
#
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(**kwargs)
#         context['form'] = CartAddProductionForm
#         return context
