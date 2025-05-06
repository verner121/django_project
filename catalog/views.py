from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Контактные данные и сообщение получены"
                            f"Ваше имя: {name}, номер телефона: {phone}, сообщение: {message}")
    return render(request, 'contacts.html')
