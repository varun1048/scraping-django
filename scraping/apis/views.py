from email import message
from urllib.error import HTTPError
from django.shortcuts import render,HttpResponse
from .models import Product
from .soup.flipkartSoup import flipkartScraping
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from urllib.parse import urlparse

from .constant import SupportedDomains
class IndexView(View):
    @csrf_exempt
    def get(self ,req, *args, **kwargs):
        return render(req,"index.html")
    
    @csrf_exempt
    def post(self,req ,*args, **kwargs):
        url =  req.POST.get("url")
        parsed_url = urlparse(url)
        if parsed_url.netloc.find(SupportedDomains.FLIPKART.value) != -1:
            result = flipkartScraping(url)
            for product in result[::-1]:
                Product.objects.create(**product)
            return JsonResponse({"list":result},status=200)
        else:
            return JsonResponse({"error":True,"message":"UnSupported URL. We support only flipkart."},status=404)

class ProductList(ListView):
    model = Product



