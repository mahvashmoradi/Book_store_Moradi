from django.urls import path
from .views import home, HomeView, ProductDetailView
app_name = 'app.pages'
urlpatterns = [
    # path('', home, name='home'),
    path('<int:id>/', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
