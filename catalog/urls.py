from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductsListView, ProductsDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='product_details'),
]