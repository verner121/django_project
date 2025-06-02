from django.db import models

from users.models import User
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Категория',
        help_text='Напишите категорию'
    )
    description = models.TextField(
        max_length=350,
        verbose_name='Описание категории',
        help_text='Напишите описание категории'
    )
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название товара',
        help_text='Напишите название товара'
    )
    description = models.TextField(
        verbose_name='Описание товара',
        help_text='Напишите описание товара'
    )
    image = models.ImageField(
        upload_to='product/photo',
        blank=True,
        null=True,
        verbose_name='Изображение',
        help_text='Загрузите изображение товара'
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    price = models.IntegerField(
        default=0,
        help_text='Введите цену продукта'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publication_status = models.BooleanField(default=False)

    owner = models.ForeignKey(User, verbose_name='Владелец', help_text='Укажите владельца продукта', blank=True,
                              null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['price', 'name', 'category']
        indexes = [
            models.Index(fields=["name", "category"]),
        ]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product')
        ]

    def __str__(self):
        return self.name
