from django.urls import path
from .views import  *
app_name = 'app.cart'
urlpatterns = [
    # path('', home, name='home'),
    path('add/<int:product_id>/', AddCart.as_view(), name='add_cart'),
    path('', DetailCart.as_view(), name='cart_detail'),
    path('remove/<int:product_id>/', RemoveCart.as_view(), name='remove_cart'),

]
