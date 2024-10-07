from django.urls import path, include, re_path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewSet)



urlpatterns = [
    path('products/', ProductListCreateApiView.as_view(), name = 'products'),
    path('', include(router.urls)), #
    path('drf-auth/', include('rest_framework.urls')),
    path('^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product2')
    # path('list/', ProductListApiView.as_view(), name = 'list'),
    # path('create/', ProductCreateApiView.as_view(), name = 'create'),
    # path('product/<int:pk>/', ProductRetrieveApiView.as_view(), name = 'product'),
]


