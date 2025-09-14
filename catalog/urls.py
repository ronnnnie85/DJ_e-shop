from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='product_details'),
    path('products/new/', ProductsCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductsUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='product_delete'),
]