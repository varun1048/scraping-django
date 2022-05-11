from django.db import models

# Create your models here.
class Product(models.Model):
    
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    price = models.CharField(max_length=20)  
    description = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    date =  models.DateField(auto_now_add=True)
    
