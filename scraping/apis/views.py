from django.shortcuts import render
from .flipkart import flipkart_prodect
from .scraping import scrape_flipkart
from .models import Product
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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