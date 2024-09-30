from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    price = models.DecimalField('Цена', max_length=100, decimal_places=2, max_digits=4)
    description = models.TextField('Описание', blank=True, null=True)
    quantity = models.PositiveIntegerField('Количество', default=0)
    createad_at = models.DateTimeField('Дата создания', blank=True, null=True )
    is_active = models.BooleanField('Активен', default = True)



