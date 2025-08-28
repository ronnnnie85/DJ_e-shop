from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, product_details, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', product_details, name='product_details'),
]