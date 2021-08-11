from django.urls import path
from .views import home, HomeView

urlpatterns = [
    # path('', home, name='home'),
    path('', HomeView.as_view(), name='home'),
]
