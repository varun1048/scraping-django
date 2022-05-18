from django.shortcuts import render
from .models import Product
from .soup.flipkartSoup import flipkartScraping
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic.edit import DeleteView

from urllib.parse import urlparse

from .constant import SupportedDomains
class IndexView(View):
   
    @csrf_exempt
    def post(self,req ,*args, **kwargs):
        url =  req.POST.get("url")
        parsed_url = urlparse(url)
        if parsed_url.netloc.find(SupportedDomains.FLIPKART.value) != -1:
            result = flipkartScraping(url)
            for product in result:
                Product.objects.create(**product)
            return JsonResponse({"list":result},status=200)
        else:
            return JsonResponse({"error":True,"message":"UnSupported URL. We support only flipkart."},status=404)


class ProductList(ListView):
    model = Product



class ProductDetail(DetailView):
    model = Product
    

class ProductDelete(DeleteView):
    model = Product
    success_url ="/"
    


