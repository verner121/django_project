from django import forms
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView

from catalog.forms import ProductForm
from catalog.models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:product_list')

