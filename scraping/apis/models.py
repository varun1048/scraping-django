from django.db import models

# Create your models here.
class    hamrobazaar(models.Model):
    
    ulr = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    price = models.IntegerField()  
    mobile_number =     models.CharField(max_length=10)
    
