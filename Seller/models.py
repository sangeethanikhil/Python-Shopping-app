from django.db import models
from Admin.models import *
from Buyer.models import *

# Create your models here.

class seller_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20)

class image_tb(models.Model):
    category_id=models.ForeignKey(category_tb,on_delete=models.CASCADE)
    seller_id=models.ForeignKey(seller_tb,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    details=models.CharField(max_length=20)
    stock=models.CharField(max_length=20)
    price=models.FloatField(max_length=20)
    image=models.FileField()

class track_tb(models.Model):
    order_id=models.ForeignKey('Buyer.order_tb',on_delete=models.CASCADE)
    trackingdetails=models.CharField(max_length=100)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)

    
