from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


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


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html', context)
