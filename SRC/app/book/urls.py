from django.urls import path
from app.book.views import *
app_name = 'app.book'

urlpatterns = [
    path('books/', BookView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book-edit/<int:pk>/', BookEditView.as_view(), name='book_edit'),
    path('book-delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('add-book/', AddBookView.as_view(), name='add_book'),
    path('add-categoty/', AddCategoryView.as_view(), name='add_category'),
    path('<int:pk>/delete_categories/', CategoriesDeleteView.as_view(), name='categories_delete'),
    path('<int:pk>/edit_categories/', CategoriesEditView.as_view(), name='categories_edit'),
    path('Categories/', CategoriesView.as_view(), name='categories_list'),
    path('Categories/<int:pk>/', CategoriesDetailView.as_view(), name='categories_item'),
    path('authors/', AuthorView.as_view(), name='author_list'),
    path('author-edit/<int:pk>/', AuthorUpdateView.as_view(), name='author_edit'),
    path('author-delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
    path('add-author/', AddAuthorView.as_view(), name='add_author'),
]
