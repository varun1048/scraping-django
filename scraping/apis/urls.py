from django.contrib import admin
from django.urls import path
from . import views

from .views import IndexView,ProductsView
# urlpatterns = [
#     path('', views.index),
#     path('product', views.product),           
#     path('test', views.test),           
# ]


urlpatterns = [
    path('', IndexView.as_view(),name="index"),
    path("products",ProductsView.as_view(),name="products")
]
