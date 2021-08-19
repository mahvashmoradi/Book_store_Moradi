from django.urls import path
from .views import  ProductDetailView, HomeView
app_name = 'app.pages'
urlpatterns = [
    # path('home', home, name='home'),
    path('<int:id>/', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    # path('search/', search_book, name='search'),
]
