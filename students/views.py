from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'students/contact.html')