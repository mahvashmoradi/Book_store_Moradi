from django.db.models import Count
from django.shortcuts import  get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import BookForm
from .models import BookModel, CategoryModel, Author
from app.accounts.Mixin import GroupRequiredMixin
from ..payment.models import Discount, Coupons
# Create your views here.


class BookView(GroupRequiredMixin, ListView):
    """
    لیست کتاب ها
    """
    model = BookModel
    # queryset = Task.objects.all()
    template_name = 'book/book_ope/book_list.html'
    group_required = [u'staff_group', u'admin_group']


class AuthorView(GroupRequiredMixin, ListView):
    """
    لیست نویسندگان
    """
    model = Author
    # queryset = Task.objects.all()
    template_name = 'book/author/author_list.html'
    group_required = [u'staff_group', u'admin_group']


class BookDetailView(GroupRequiredMixin, DetailView):
    """
    جزییات هر کتاب
    """
    model = BookModel
    template_name = 'book/book_ope/book_detail.html'
    group_required = [u'staff_group', u'admin_group']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = get_object_or_404(BookModel, pk=self.kwargs['pk'])
        context['categories'] = book_id.categories.all()
        return context


class BookEditView(GroupRequiredMixin, UpdateView):
    """
    ویرایش اطلاعات کتاب
    """
    model = BookModel
    # fields = ('title', 'description',)
    fields = '__all__'
    template_name = 'book/book_ope/book_edit.html'
    success_url = reverse_lazy('book:book_list')
    group_required = [u'staff_group', u'admin_group']


class AuthorUpdateView(GroupRequiredMixin, UpdateView):
    """
    ویرایش اطلاعات نویسنده
    """
    model = Author
    # fields = ('title', 'description',)
    fields = '__all__'
    template_name = 'book/author/author_edit.html'
    success_url = reverse_lazy('book:author_list')
    group_required = [u'staff_group', u'admin_group']


class BookDeleteView(GroupRequiredMixin, DeleteView):
    """
    حذف کتاب
    """
    model = BookModel
    template_name = 'book/book_ope/book_delete.html'
    success_url = reverse_lazy('book:book_list')
    group_required = [u'staff_group', u'admin_group']


class AuthorDeleteView(GroupRequiredMixin,DeleteView):
    """
    حذف نویسنده
    """
    model = Author
    template_name = 'book/author/author_delete.html'
    success_url = reverse_lazy('book:author_list')
    group_required = [u'staff_group', u'admin_group']


# class AddBookView(View):
#     def get(self, request):
#         form = BookForm
#         return render(request, 'book/book_add.html', {'form' : form})
#     def post(self, request, *args, **kwargs):
#         form = BookForm(request.POST or None)
#         if form.is_valid():
#             book = BookModel.objects.create(name=request.POST['name'], price=request.POST['price'],
#                                             inventory=request.POST['inventory'], image = request.POST['image'])
#             author_list = list(map(lambda x: x.strip(),form.cleaned_data['author'].split("|")))
#             categories_list = list(map(lambda x: x.strip(),form.cleaned_data['categories'].split("|")))
#
#             # print(author_list)
#             # print(categories_list)
#             for author_name in author_list:
#                 author, created = Author.objects.get_or_create(name=author_name)
#                 book.author.add(author)
#                 book.save()
#
#             for category_name in categories_list:
#                 category, created = CategoryModel.objects.get_or_create(name=category_name)
#                 book.categories.add(category)
#                 book.save()
#         return redirect('./')


class AddBookView(GroupRequiredMixin,CreateView):
    """
    افزودن کتاب
    """
    # form_class = BookForm
    model = BookModel
    fields = '__all__'
    success_url = reverse_lazy('book:book_list')
    template_name = 'book/book_ope/book_add.html'
    group_required = [u'staff_group', u'admin_group']


class AddAuthorView(GroupRequiredMixin,CreateView):
    """
    افزودن نویسنده
    """
    # form_class = BookForm
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('book:author_list')
    template_name = 'book/author/author_add.html'
    group_required = [u'staff_group', u'admin_group']


#     #
#     def form_valid(self, form):
#         book = form.save(commit=False)
#         author_list = form.cleaned_data['author'].split(",")
#         categories_list = form.cleaned_data['categories'].split(",")
#         for author_name in author_list:
#             author, created = Author.objects.get_or_create(name=author_name)
#             book.author.add(author.name)
#             # book.save()
#
#         for category_name in categories_list:
#             category, created = CategoryModel.objects.get_or_create(name=category_name)
#             book.categories.add(category.name)
#             # categories.save()
#         return super(AddBookView, self).form_valid(form)


class AddCategoryView(GroupRequiredMixin,CreateView):
    """
    ایجاد دسته بندی
    """
    # form_class = CategoryForm
    model = CategoryModel
    fields = '__all__'
    success_url = reverse_lazy('accounts:staff_menu')
    template_name = 'book/categoty/category_add.html'
    group_required = [u'staff_group', u'admin_group']


class CategoriesView(GroupRequiredMixin,ListView):
    """
    لیست دسته بندی ها، تفکیک شده بر اساس پر و خالی بودن
    """
    model = CategoryModel
    template_name = 'book/categoty/category_list.html'
    group_required = [u'staff_group', u'admin_group']

    # queryset = Categories.objects.annotate(c=Count('categories_item')).filter(c__gt=0)
    # queryset = Categories.categories_manager.empty()
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of empty category and full category
        context['empty_categories'] = CategoryModel.objects.annotate(c=Count('category')).filter(c=0)
        context['full_categories'] = CategoryModel.objects.annotate(c=Count('category')).filter(c__gt=0)
        return context


class CategoriesDetailView(GroupRequiredMixin,DetailView):
    """
    نشان دادن آیتم های هر دسته بندی
    """
    model = CategoryModel
    template_name = 'book/categoty/categories_item.html'
    group_required = [u'staff_group', u'admin_group']

    def get_object(self):
        course = get_object_or_404(CategoryModel, pk=self.kwargs['pk'])
        return course.category.all()


class CategoriesEditView(GroupRequiredMixin,UpdateView):
    """
    ویرایش اطلاعات دسته بندی ها
    """
    model = CategoryModel
    # fields = ('title', 'body',)
    fields = '__all__'
    template_name = 'book/categoty/categories_edit.html'
    success_url = reverse_lazy('book:categories_list')
    group_required = [u'staff_group', u'admin_group']


class CategoriesDeleteView(GroupRequiredMixin,DeleteView):
    """
    پاک کردن دسته بندی
    """
    model = CategoryModel
    template_name = 'book/categoty/categories_delete.html'
    success_url = reverse_lazy('book:categories_list')
    group_required = [u'staff_group', u'admin_group']
