from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True, null=True)
    createad_at = models.DateTimeField('Дата создания', blank=True, null=True)

class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    price = models.DecimalField('Цена', max_length=100, decimal_places=2, max_digits=4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    quantity = models.PositiveIntegerField('Количество', default=0)
    createad_at = models.DateTimeField('Дата создания', blank=True, null=True )
    is_active = models.BooleanField('Активен', default = True)



