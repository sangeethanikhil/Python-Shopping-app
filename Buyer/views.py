from django.shortcuts import render
from Buyer.models import *
from Seller.models import *
from Admin.models import *
import datetime

# Create your views here.
def register(request):
    return render(request,'register.html')

def registerAction(request):
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
        return render(request,'register.html',{'msg':"user name already exist"})
    else:
        user=register_tb(name=name,gender=gender,address=address,country=country,phone=phone,username=username,password=password)
        user.save()
    return render(request,'register.html',{'msg':"registered successfully"})
    
def viewproducts(request):
    product=image_tb.objects.all()
    return render(request,'viewProducts.html',{'data':product})

def addtocart(request,prid):
    cart=image_tb.objects.filter(id=prid)
    return render(request,'addtocart.html',{'data':cart})

def cartAction(request):
    product_id=request.POST['product_id']
    buyer_id=request.session['buyer_id']
    product=image_tb.objects.filter(id=product_id)
    seller_id=product[0].seller_id
    address=request.POST['address']
    number=request.POST['number']
    quantity=request.POST['quantity']
    price=request.POST['price']
    buyers=register_tb.objects.get(id=buyer_id)
    products_id=image_tb.objects.get(id=product_id)
    product_stock=product[0].stock
    if int(quantity)>int(product_stock):
        msg={'msg':"out of limit",'data':product}
    else:
        cart=cart_tb(product_id=products_id,buyer_id=buyers,seller_id=seller_id,address=address,number=number,quantity=quantity,price=price)
        cart.save()
        msg={'msg':"uploaded successfully",'data':product}
    return render(request,'addtocart.html',msg)

def viewcart(request):
    buyer_id=request.session['buyer_id']
    cart=cart_tb.objects.filter(buyer_id=buyer_id)
    return render(request,'viewcart.html',{'data':cart})

def remove(request,cid):
    removes=cart_tb.objects.filter(id=cid).delete()
    remov=cart_tb.objects.all()
    return render(request,'viewcart.html',{'data':remov})

def confirm(request,oid):
    order=cart_tb.objects.filter(id=oid)
    product_id=order[0].product_id
    buyer_id=order[0].buyer_id
    seller_id=order[0].seller_id
    address=order[0].address
    number=order[0].number
    quantity=order[0].quantity
    price=order[0].price
    date=datetime.date.today()
    stk=product_id.stock
    ordr=cart_tb.objects.filter(buyer_id=buyer_id)
    if int(stk)<int(quantity):
       msg={'msg':"insufficient stock",'data':ordr}
    else:
        product_stock=product_id.stock
        stock=int(product_stock)-int(quantity)
        product_id.stock=stock
        product_id.save()
        orders=order_tb(product_id=product_id,buyer_id=buyer_id,seller_id=seller_id,address=address,number=number,quantity=quantity,price=price,date=date,status='pending')
        orders.save()
        product=cart_tb.objects.filter(id=oid).delete()
        msg={'msg':"confirmed",'data':ordr}
    return render(request,'viewcart.html',msg)

def vieworders(request):
    buyer_id=request.session['buyer_id']
    order=order_tb.objects.filter(buyer_id=buyer_id)
    return render(request,'vieworders.html',{'data':order})

def cancel(request,caid):
    buyer_id=request.session['buyer_id']
    order=order_tb.objects.filter(id=caid)
    order.update(status='cancelled')
    order=order_tb.objects.filter(buyer_id=buyer_id)
    return render(request,'vieworders.html',{'data':order})

def viewtrackingdetails(request,tid):
    track=track_tb.objects.filter(order_id=tid).order_by('-id')
    return render(request,'viewtrackingdetails.html',{'data':track})

def productSearch(request):
    name=request.POST['name']
    product=image_tb.objects.filter(name__startswith=name)
    return render(request,'viewproducts.html',{'data':product})
    
def searchbyprice(request):
    category=category_tb.objects.all()
    return render(request,'searchbyprice.html',{'data':category})

def priceAction(request):
    category_id=request.POST['category']
    price=request.POST['price']
    prices=image_tb.objects.filter(category_id=category_id,price__lte=float(price))
    return render(request,'viewproducts.html',{'data':prices})

def viewprofile(request):
    pid=request.session['buyer_id']
    profile=register_tb.objects.filter(id=pid)
    return render(request,'updateprofile.html',{'data':profile})

def profileAction(request):
    pid=request.session['buyer_id']
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    profile=register_tb.objects.filter(id=pid)
    profile.update(name=name,gender=gender,address=address,country=country,phone=phone,username=username)
    return render(request,'updateprofile.html',{'data':profile,'msg':"updated sucessfully"})


def forgottenpassword(request):
    return render(request,'forgottenpassword.html')

def passwordAction(request):
    username=request.POST['username']
    pswd=register_tb.objects.filter(username=username)
    pswd1=seller_tb.objects.filter(username=username)
    if pswd.count()>0:
        return render(request,'passwordDetails.html',{'data':username})
    elif pswd1.count()>0:
        return render(request,'passwordDetails.html',{'data':username})
    
    else:
        msg={'msg':"incorrect username"}
        return render(request,'login.html',msg)
    

def checkDetails(request):
    username=request.POST['username']
    name=request.POST['name']
    country=request.POST['country']
    phone=request.POST['phone']
    pswd=register_tb.objects.filter(username=username,name=name,country=country,phone=phone)
    pswd1=seller_tb.objects.filter(username=username,name=name,country=country,phone=phone)
    if pswd.count()>0:
        return render(request,'newpassword.html',{'data':username})
    elif pswd1.count()>0:
        return render(request,'newpassword.html',{'data':username})
    else:
        msg={'msg':"invalid details"}
        return render(request,'passwordDetails.html',msg)
def passwordUpdate(request):
    username=request.POST['username']
    password=request.POST['password']
    reenterpassword=request.POST['reenterpassword']
    confirm=register_tb.objects.filter(username=username)
    confirm1=seller_tb.objects.filter(username=username)
    if password==reenterpassword:
        if confirm.count()>0:
            confirm.update(password=password)
            msg={'msg':"updated successfully",'data':username}
            return render(request,'login.html',msg)
        else:
            confirm1.update(password=password)
            msg={'msg':"updated successfully",'data':username}
            return render(request,'login.html',msg)
    else:
        msg={'msg':"unmatched password",'data':username}
        return render(request,'newpassword.html',msg)
            
        
        
    


    

    
    
    
    
