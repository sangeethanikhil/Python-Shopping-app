from django.shortcuts import render,redirect
from Seller.models import *
from Buyer.models import *
from Admin.models import *



# Create your views here.
def index(request):
    context={}
    if 'buyer_id' in request.session:
        product=image_tb.objects.all()[:5]
        context['data']=product
    elif 'seller_id' in request.session:
        seller_id=request.session['seller_id']
        order=order_tb.objects.filter(seller_id=seller_id)[:5]
        context['data']=order
        
    elif 'admin_id' in request.session:
         seller=seller_tb.objects.all()[:5]
         context['data']=seller
        
    return render(request,'index.html',context)
def login(request):
     return render(request,'login.html')

def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=login_tb.objects.filter(username=username,password=password)
    user1=register_tb.objects.filter(username=username,password=password)
    user2=seller_tb.objects.filter(username=username,password=password)
    if user.count()>0:
        request.session['admin_id']=user[0].id
        return redirect('index')
    elif user1.count()>0:
        request.session['buyer_id']=user1[0].id
        return redirect('index')
    
    elif user2.count()>0:
        
        if user2[0].status=='Approved':
            request.session['seller_id']=user2[0].id
            return redirect('index')
        else:
            return render(request,'login.html',{'msg':"Not a Valid Seller"})
    else:
        
        return render(request,'login.html',{'msg':"incorrect username or password"})

def addCategory(request):
    return render(request,'addCategory.html')

def categoryAction(request):
    add=request.POST['add']
    user=category_tb(add=add)
    user.save()
    return render(request,'addCategory.html',{'msg':"Added successfully"})

def viewSellers(request):
    seller=seller_tb.objects.all()
    return render(request,'viewSellers.html',{'data':seller})

def approve(request,sid):
    ap=seller_tb.objects.filter(id=sid)
    ap.update(status='Approved')
    ap=seller_tb.objects.all()
    return render(request,'viewSellers.html',{'data':ap})

def reject(request,sid):
    ap=seller_tb.objects.filter(id=sid)
    ap.update(status='Rejected')
    ap=seller_tb.objects.all()
    return render(request,'viewSellers.html',{'data':ap})

def logout(request):
    if 'buyer_id' in request.session:
        del request.session['buyer_id']
    elif 'seller_id' in request.session:
        del request.session['seller_id']
    else:
        del request.session['admin_id']
    return render(request,'index.html')
    
    
    
    
