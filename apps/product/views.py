# from itertools import product
#
# from django.contrib.gis.db.backends.postgis.const import POSTGIS_TO_GDAL
# from django.core.serializers import serialize
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.core.serializers import serialize
from django.template.defaulttags import querystring
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category
from .serializers import ProductSerializer
from rest_framework import generics, mixins, viewsets
from .custom_views import *
from .custom_permission import IsOwnerOrReadOnly
class ProductViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet): # ModelViewSet
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsOwnerOrReadOnly]

# --------------------------------------------------------
    @action(methods=['get'], detail = False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})

    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.all().values()
    #     return Response({'cats': [cats]})

    # @action(methods=['get'], detail = False)
    # def category(self, request):
    #     cats = Category.objects.all().values()
    #     return Response({'cats': [cats]})
#--------------------------------------------------------



#--------------------------------------------------------
# class ProductViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many = True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk = None):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#--------------------------------------------------------

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#
# class ProductListApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductCreateApiView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductRetrieveApiView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductUpdateDestroyApiview(CustomUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# #
# class ProductView(APIView):
#     def get(self, request):
#         n = Product.objects.all()
#         return Response({'product': ProductSerializer(n, many = True).data})  #many = True сериализация  данных # many = False pk = pk или id
#
#
#     def post(self, request):
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception = True) # проверка на валидность
#
#         product = Product.objects.create(
#             name = serializer.validated_data['name'],
#             price = serializer.validated_data['price'],
#             description = serializer.validated_data['description'],
#             quantity = serializer.validated_data['quantity'],
#             is_active = serializer.validated_data['is_active']
#         )
#         return Response({'product': ProductSerializer(product).data})
#
#
#
#
#
#






# # Methods:
# # GET - получить данные
# # POST - создать/отправить данные
# # PUT - изменить данные
# # DELETE - удалить данные
# # PATCH - изменить данные частично
# # HEAD - получить заголовки
# # OPTIONS - получить доступные методы

