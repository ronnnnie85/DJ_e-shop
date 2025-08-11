from django.db import models

class Product(models.Model):
    # наименование,
    # описание,
    # изображение,
    # категория,
    # цена
    # за
    # покупку,
    # дата
    # создания,
    # дата
    # последнего
    # изменения.
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование товара')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание товара')
    picture = models.ImageField(upload_to='catalog/photo/', blank=True, null=True, verbose_name='Изображение', help_text='Загрузите изображение товара')
