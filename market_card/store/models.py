from django.db import models

class Product(models.Model):
 image_path = models.CharField(max_length=200) 
 title = models.CharField(max_length=50) 
 description = models.TextField() 
 price = models.DecimalField(decimal_places=2, max_digits=100)

