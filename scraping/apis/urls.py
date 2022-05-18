from django.urls import path


from .views import IndexView,ProductList,ProductDetail,ProductDelete

urlpatterns = [
    path('', IndexView.as_view(),name="index"),
    path("products",ProductList.as_view(),name="products"),
    path("detail/<str:pk>",ProductDetail.as_view(),name="Detail"),
    path("delete/<str:pk>",ProductDelete.as_view(),name="Detail"),
]
