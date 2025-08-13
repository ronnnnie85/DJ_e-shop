from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование товара')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание товара')
    picture = models.ImageField(upload_to='catalog/photo/', blank=True, null=True, verbose_name='Изображение', help_text='Загрузите изображение товара')
    category = models.ForeignKey(on_delete=models.SET_NULL, verbose_name="Категория", help_text="Введите категорию товара", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text="Введите цену")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", help_text="Введите дату создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения", help_text="Введите дату изменения")

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['category', 'name']


    def __str__(self):
        return f'{self.category} - {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование категории')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание категории')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


    def __str__(self):
        return f'{self.name}'