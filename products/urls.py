from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
]
# This URL configuration maps the 'products/' endpoint to the ProductListView, which will handle GET requests to list products.