from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email адрес")
    phone_number = models.CharField(max_length=15, verbose_name="Телефон" , blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name="Аватар", blank=True, null=True)
    country = CountryField(blank=True, null=True)
    token = models.CharField(blank=True, null=True, max_length=100, verbose_name="Токен")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
