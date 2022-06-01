from django.db import models
from Seller.models import *
# Create your models here.
class register_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class cart_tb(models.Model):
    product_id=models.ForeignKey(image_tb,on_delete=models.CASCADE)
    buyer_id=models.ForeignKey(register_tb,on_delete=models.CASCADE,default=2)
    seller_id=models.ForeignKey(seller_tb,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    number=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=20)

class order_tb(models.Model):
    product_id=models.ForeignKey(image_tb,on_delete=models.CASCADE)
    buyer_id=models.ForeignKey(register_tb,on_delete=models.CASCADE,default=2)
    seller_id=models.ForeignKey(seller_tb,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    number=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
