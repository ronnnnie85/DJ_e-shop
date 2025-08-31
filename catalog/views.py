from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


# Create your views here.
class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Обработка данных
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение '{message}' и телефон {phone} получено.")


class ProductsListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'
