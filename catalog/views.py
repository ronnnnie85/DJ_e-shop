from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

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

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_details.html', context)