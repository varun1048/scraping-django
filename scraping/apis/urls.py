from django.urls import path
from django.views.generic import TemplateView
from .views import IndexView,ProductList,ProductDetail,ProductDelete

urlpatterns = [
    
    path('',TemplateView.as_view(template_name="index.html"),name="index"),
    path('scraping',IndexView.as_view(),name="scraping"),
    
    path("products",ProductList.as_view(),name="products"),
    path("detail/<str:pk>",ProductDetail.as_view(),name="detail"),
    path("delete/<str:pk>",ProductDelete.as_view(),name="delete"),
]
