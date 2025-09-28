from django.urls import path, include
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView, ProductsPublicatedView, CategoryListView, CategoryDetailView
from config.settings import CACHE_ENABLED

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', cache_page(60)(ProductsDetailView.as_view()) if CACHE_ENABLED else ProductsDetailView.as_view(), name='product_details'),
    path('products/new/', ProductsCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductsUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/no_publicate/', ProductsPublicatedView.as_view(), name='product_not_public'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_details'),
]