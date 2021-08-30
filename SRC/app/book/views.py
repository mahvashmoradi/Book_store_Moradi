from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import BookModel, CategoryModel


# Create your views here.

class BookView(ListView):
    model = BookModel
    # queryset = Task.objects.all()
    template_name = 'book/book_list.html'


class BookDetailView(DetailView):
    model = BookModel
    template_name = 'book/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = get_object_or_404(BookModel, pk=self.kwargs['pk'])
        context['categories'] = book_id.categories.all()
        return context


class BookEditView(UpdateView):
    model = BookModel
    # fields = ('title', 'description',)
    fields = '__all__'
    template_name = 'book/book_edit.html'
    success_url = reverse_lazy('book:book_list')


class BookDeleteView(DeleteView):  # new
    model = BookModel
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('book:book_list')


class AddBookView(CreateView):
    # form_class = TaskForm
    model = BookModel
    fields = '__all__'
    success_url = reverse_lazy('book:book_list')
    template_name = 'book/book_add.html'


class AddCategoryView(CreateView):
    # form_class = CategoryForm
    model = CategoryModel
    fields = '__all__'
    success_url = reverse_lazy('accounts:staff_menu')
    template_name = 'book/category_add.html'


class CategoriesView(ListView):
    model = CategoryModel
    template_name = 'book/category_list.html'

    # queryset = Categories.objects.annotate(c=Count('categories_item')).filter(c__gt=0)
    # queryset = Categories.categories_manager.empty()
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of empty category and full category
        context['empty_categories'] = CategoryModel.categories_manager.empty()
        context['full_categories'] = CategoryModel.categories_manager.full()
        return context


class CategoriesDetailView(DetailView):
    model = CategoryModel
    template_name = 'book/categories_detail.html'

    def get_object(self):
        course = get_object_or_404(CategoryModel, pk=self.kwargs['pk'])
        return course.category.all()


class CategoriesEditView(UpdateView):
    model = CategoryModel
    # fields = ('title', 'body',)
    fields = '__all__'
    template_name = 'book/categories_edit.html'
    success_url = reverse_lazy('book:categories_list')


class CategoriesDeleteView(DeleteView):  # new
    model = CategoryModel
    template_name = 'book/categories_delete.html'
    success_url = reverse_lazy('book:categories_list')
