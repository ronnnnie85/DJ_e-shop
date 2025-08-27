from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} и телефон {phone} получено.")
    return render(request, 'contacts.html')