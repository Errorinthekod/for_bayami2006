from django.urls import path, include
from .views import *


urlpatterns = [
    path('test/', ProductView.as_view(), name = 'test')
]


