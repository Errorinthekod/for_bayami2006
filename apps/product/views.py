from django.contrib.gis.db.backends.postgis.const import POSTGIS_TO_GDAL
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductView(APIView):
    def get(self, request):
        n = Product.objects.all()
        return Response({'product': ProductSerializer(n, many = True).data})

    def post(self, request):
        return Response({'title': 'Hello World2 from post'})







# Methods:
# GET - получить данные
# POST - создать/отправить данные
# PUT - изменить данные
# DELETE - удалить данные
# PATCH - изменить данные частично
# HEAD - получить заголовки
# OPTIONS - получить доступные методы







