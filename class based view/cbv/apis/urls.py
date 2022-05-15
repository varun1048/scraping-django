from unicodedata import name
from django.urls import path
from .views import index,Ex2

from django.views.generic import TemplateView,RedirectView

app_name= "apis"

urlpatterns = [
    path('',index,name="index"),
    path("ex1",TemplateView.as_view(template_name="ex1.html",extra_context={"title":"clas based view"})),
    path("ex2",Ex2.as_view(),name="ex2"),
    path("rdc",RedirectView.as_view(url="https://www.youtube.com/watch?v=b4r_LufNQNk"),name="rdc")
    
]
