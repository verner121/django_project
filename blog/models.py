from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок')

    description = models.TextField(
        verbose_name='Содержимое ')
    image = models.ImageField(
        upload_to='blog/photo',
        blank=True,
        null=True,
        verbose_name='Превью' )
    created_at = models.DateTimeField(auto_now_add=True)
    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        default=0)
    publication_attribute = models.BooleanField(default=True)


class Meta:
    verbose_name = 'Блог'
    verbose_name_plural = 'Блоги'
    ordering = ['title', 'publication_attribute', 'views_count']


def __str__(self):
    return self.title
