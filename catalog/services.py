from itertools import product

from django.core.cache import cache
from django.shortcuts import get_object_or_404

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


class ProductService:
    @staticmethod
    def get_products_by_category(category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        return products



def get_products_from_cache():
    """Получает список продуктов из кэша, если кэш пуст то получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
