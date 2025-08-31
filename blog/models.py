from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    content = models.TextField(
        verbose_name="Содержимое", help_text="Введите содержимое"
    )
    preview = models.ImageField(
        upload_to="blog/images/",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    publicated = models.BooleanField(
        verbose_name="Опубликовано",
        default=False,
        help_text="Укажите признак публикации",
    )
    number_of_views = models.IntegerField(
        default=0, verbose_name="Количество просмотров", help_text="Укажите количество просмотров"
    )

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.title}"