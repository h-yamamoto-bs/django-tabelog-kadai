from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.shop_list, name='shop_list'),
]
