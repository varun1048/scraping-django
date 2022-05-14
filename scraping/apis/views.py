from django.shortcuts import render,HttpResponse
from .flipkart import flipkart_prodect
from .scraping import scrape_flipkart
from .models import Product
# Create your views here.
from django.http import JsonResponse

def index(req):
    if req.method == 'POST':
        form = req.POST
        for product in scrape_flipkart(form['base_url'])[::-1]:
            Product.objects.create(**product).save()        
            
        
    scraped_products = Product.objects.all()[::-1]
    return render(req,"index.html",{
        "scraped_products":scraped_products
        })  




def product(req):
    data = {}
    if req.method == 'POST':
        form = req.POST
        data = flipkart_prodect(form['base_url'])
        print(data['error'])        
        
    return render(req,"product.html",data)

def test(req):
    if req.method == 'POST':
        url =  req.POST.get("url")
        return JsonResponse({"list":scrape_flipkart(url)},status=200)