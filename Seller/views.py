from django.shortcuts import render
from Seller.models import *
from Admin.models import *
from Buyer.models import *
import datetime


# Create your views here.

def sellerRegistration(request):
    return render(request,'sellerRegistration.html')


def sellerregisterAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    user1=seller_tb.objects.filter(username=username)
    user2=login_tb.objects.filter(username=username)
    user3=register_tb.objects.filter(username=username)
    if user1.count()>0 or user2.count()>0 or user3.count()>0:
        return render(request,'sellerRegister.html',{'msg':"user name already exist"})
    else:
        user=seller_tb(name=name,gender=gender,address=address,country=country,phone=phone,username=username,password=password,status="pending")
        user.save()
    return render(request,'sellerRegistration.html',{'msg':"registered successfully"})

def addProduct(request):
    cate=category_tb.objects.all()
    return render(request,'addProduct.html',{'data':cate})

def productAction(request):
    seller_id=request.session['seller_id']
    name=request.POST['name']
    category_id=request.POST['category']
    details=request.POST['details']
    stock=request.POST['stock']
    price=request.POST['price']
    category=category_tb.objects.get(id=category_id)
    seller=seller_tb.objects.get(id=seller_id)
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image="no pic"
    user=image_tb(seller_id=seller,name=name,category_id=category,details=details,stock=stock,price=price,image=image)
    user.save()
    category1=category_tb.objects.all()
    return render(request,'addProduct.html',{'data':category1,'msg':"uploaded successfully"})

def viewProduct(request):
    product=image_tb.objects.all()
    return render(request,'viewProduct.html',{'data':product})

def updateProduct(request,pid):
    product=image_tb.objects.filter(id=pid)
    user=category_tb.objects.all()
    return render(request,'updateProduct.html',{'data':product,'category':user})

def updateAction(request):
    pid=request.POST['pid']
    name=request.POST['name']
    category_id=request.POST['category']
    details=request.POST['details']
    stock=request.POST['stock']
    price=request.POST['price']
    product=image_tb.objects.get(id=pid)
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image=product.image
    product.name=name
    product.category=category_tb.objects.get(id=category_id)
    product.details=details
    product.stock=stock
    product.price=price
    product.image=image
    product.save()
    product=image_tb.objects.filter(id=pid)
    return render(request,'updateProduct.html',{'data':product,'msg':"updated successfully"})
    
def deleteProduct(request,pid):
    product=image_tb.objects.filter(id=pid).delete()
    products=image_tb.objects.all()
    return render(request,'viewProduct.html',{'data':products})

def vieworder(request):
    seller_id=request.session['seller_id']
    order=order_tb.objects.filter(seller_id=seller_id)
    return render(request,'vieworder.html',{'data':order})

def approves(request,cid):
    seller_id=request.session['seller_id']
    order=order_tb.objects.filter(id=cid)
    status=order[0].status
    order.update(status='approved')
    order=order_tb.objects.filter(seller_id=seller_id)
    return render(request,'vieworder.html',{'data':order})

def rejects(request,rid):
    seller_id=request.session['seller_id']
    order=order_tb.objects.filter(id=rid)
    status=order[0].status
    order.update(status='rejected')
    order=order_tb.objects.filter(seller_id=seller_id)
    return render(request,'vieworder.html',{'data':order})

def verifycancel(request,rid):
    seller_id=request.session['seller_id']
    order=order_tb.objects.filter(id=rid)
    status=order[0].status
    quantity=order[0].quantity
    product=order[0].product_id
    stock=product.stock
    order.update(status='cancelverified')
    stock=stock+quantity
    product.stock=stock
    product.save()
    order=order_tb.objects.filter(seller_id=seller_id)
    return render(request,'vieworder.html',{'data':order})

def addtrackingdetails(request,order_id):
    track=order_tb.objects.filter(id=order_id)
    return render(request,'addtrackingdetails.html',{'data':track})

def trackAction(request):
    seller_id=request.session['seller_id']
    order_id=request.POST['order_id']
    trackingdetails=request.POST['trackingdetails']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    orders_id=order_tb.objects.get(id=order_id)
    track=track_tb(order_id=orders_id,trackingdetails=trackingdetails,date=date,time=time)
    track.save()
    order=order_tb.objects.filter(id=order_id)
    if 'delivered' in trackingdetails:
        order.update(status='delivered')
        order=order_tb.objects.filter(seller_id=seller_id)
    return render(request,'vieworder.html',{'data':order,'msg':"uploaded successfully"})
    

def updateSeller(request):
    seller_id=request.session['seller_id']
    profile=seller_tb.objects.filter(id=seller_id)
    return render(request,'updateSeller.html',{'data':profile})

def sellerAction(request):
    seller_id=request.session['seller_id']
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    profile=seller_tb.objects.filter(id=seller_id)
    profile.update(name=name,gender=gender,address=address,country=country,phone=phone,username=username)
    return render(request,'updateSeller.html',{'data':profile,'msg':"updated successfully"})
    

