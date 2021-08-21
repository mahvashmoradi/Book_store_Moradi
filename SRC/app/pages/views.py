from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from django.shortcuts import render
from django.views import View

from app.accounts.models import Customer
from app.book.models import BookModel, CategoryModel
from app.payment.forms import CartAddProductionForm


# def home(request):
#     return render(request, 'pages/home.html')


# class HomeView(ListView):
#     template_name = 'pages/home.html'
#     model = BookModel
# def home(request):
#     if request.method == 'POST' and request.is_ajax():
#         print(dict(request.POST.items()))  # محتویات درخواست مشاهده کنید
#         # print(request.is_ajax())  #print True
#         input_text = request.POST['inputText']
#         books = BookModel.objects.all()  # new
#         if input_text:
#             books = BookModel.objects.filter(name__contains=input_text)
#             # message = "HI " + inputText + ' now Time : '+ str(datetime.now())
#         return JsonResponse({
#             # 'message':message,
#             # 'polls':polls   #error
#             'books': list(books.values())
#         })
#     #         product = BookModel.objects.all()
#
#     return render(request,'pages/home.html',{})

# return render(request,'pages/home.html',{})
from app.payment.models import Invoice, InvoiceLine


class HomeView(View):
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
        if request.is_ajax():
            print(dict(request.POST.items()))  # محتویات درخواست مشاهده کنید
            # print(request.is_ajax())  #print True
            input_text = request.POST['inputText']
            # books = BookModel.objects.all()  # new
            # if input_text:
            #     books = BookModel.objects.filter(name__contains=input_text)
            #     if id:
            #         category = get_object_or_404(CategoryModel, id=id)
            #         books = BookModel.objects.filter(name__contains=input_text, categories=category)
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
                    books = BookModel.objects.all()  # new

            # message = "HI " + inputText + ' now Time : '+ str(datetime.now())

            return JsonResponse({
                # 'message':message,
                'books': list(books.values())
            })

        # return render(request,'pages/home.html',{})


# class ProductDetailView(DetailView):
#     model = BookModel
#     template_name = 'pages/product.html'
#
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(**kwargs)
#         context['form'] = CartAddProductionForm
#         return context

class ProductDetailView(View):
    def get(self, request, pk):
        object = get_object_or_404(BookModel, id=pk)
        form = CartAddProductionForm
        return render(request, 'pages/product.html', {'object': object, 'form': form})

    def post(self, request, pk):
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

