from django import forms
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView
from catalog.models import Product


class ContactForm(forms.Form):
    name = forms.CharField()
    phone_number = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class ContactsView(FormView):
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = '/contacts/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        return HttpResponse(f'Спасибо {name}! Сообщение отправлено.')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         return HttpResponse(f"Контактные данные и сообщение получены"
#                             f"Ваше имя: {name}, номер телефона: {phone}, сообщение: {message}")
#     return render(request, 'contacts.html')
