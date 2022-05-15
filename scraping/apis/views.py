from django.shortcuts import render,HttpResponse
from .models import Product
from .soup.flipkartSoup import flipkartScraping
from django.http import JsonResponse


# def index(req):
#     if req.method == 'POST':
#         form = req.POST
#         for product in flipkartScraping(form['base_url'])[::-1]:
#             Product.objects.create(**product).save()        
            
        
#     scraped_products = Product.objects.all()[::-1]
#     return render(req,"index.html",{
#         "scraped_products":scraped_products
#         })  




# def product(req):
#     data = {}
#     if req.method == 'POST':
#         form = req.POST
#         data = flipkartScraping(form['base_url'])
#         print(data['error'])        
        
#     return render(req,"product.html",data)

# def test(req):
#     if req.method == 'POST':
#         url =  req.POST.get("url")
        
#         result = flipkartScraping(url)

#         return JsonResponse({"list":result},status=200)
    


from django.views import View
class IndexView(View):
    def get(self ,req, *args, **kwargs):
        return render(req,"index.html")

    def post(self,req ,*args, **kwargs):
        url =  req.POST.get("url")
        result = flipkartScraping(url)
        for product in result[::-1]:
            Product.objects.create(**product)
        return JsonResponse({"list":result},status=200)

class ProductsView(View):
    def get(self ,req,):
        scraped_products = Product.objects.all()[::-1]
        return render(req,"products.html",{  "scraped_products":scraped_products })

