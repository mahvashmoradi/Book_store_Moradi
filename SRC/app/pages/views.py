from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from app.book.models import BookModel, CategoryModel
from app.cart.forms import CartAddProductionForm


def home(request):
    return render(request, 'pages/home.html')


# class HomeView(ListView):
#     template_name = 'pages/home.html'
#     model = BookModel

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


class ProductDetailView(DetailView):
    model = BookModel
    template_name = 'pages/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = CartAddProductionForm
        return context
