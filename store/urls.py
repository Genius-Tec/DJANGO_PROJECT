from django.urls import path
from .views import product_list

urlpatterns = [
    path('', product_list, name='product_list'),
    # Add more URL patterns as needed
]
