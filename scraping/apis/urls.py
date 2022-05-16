from django.urls import path


from .views import IndexView,ProductList

urlpatterns = [
    path('', IndexView.as_view(),name="index"),
    path("products",ProductList.as_view(),name="products")
]
