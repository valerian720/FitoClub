from django.db import models
from django.core.validators import RegexValidator

# ORM сущности для хранения информации  по производителям

class ProductType(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование типа продукта')

    def __str__(self):
            return self.name
    class Meta:
        verbose_name = 'тип продуктов'
        verbose_name_plural = 'типы продуктов'


class Producer(models.Model):
    name = models.CharField(max_length=200, verbose_name='производитель')
    product_types = models.ManyToManyField(ProductType, verbose_name='типы продуктов')

    def __str__(self):
            return self.name
    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'     

# https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
class Phone(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Номер телефона должен быть в формате: '+999999999'. доступно до 15 знаков.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='номер телефона') # validators should be a list
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='производитель')

    def __str__(self):
            return self.phone_number
    class Meta:
        verbose_name = 'номер телефона'
        verbose_name_plural = 'номера телефонов'


class Email(models.Model):
    email = models.EmailField(max_length=200, verbose_name='номер электронной почты')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='производитель')

    def __str__(self):
            return self.email
    class Meta:
        verbose_name_plural = 'номера электронной почты'
        verbose_name = 'номер электронной почты'
