"""Shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Admin import views as admin_view
from Buyer import views as buyer_view
from Seller import views as seller_view
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',admin_view.index,name='index'),
    url(r'^register/',buyer_view.register,name='register'),
    url(r'^registerAction/',buyer_view.registerAction,name='registerAction'),
    url(r'^sellerRegistration/',seller_view.sellerRegistration,name='sellerRegistration'),
    url(r'^sellerregisterAction/',seller_view.sellerregisterAction,name='sellerregisterAction'),
    url(r'^login/',admin_view.login,name='login'),
    url(r'^loginAction/',admin_view.loginAction,name='loginAction'),
    url(r'^addCategory/',admin_view.addCategory,name='addCategory'),
    url(r'^categoryAction/',admin_view.categoryAction,name='categoryAction'),
    url(r'^addProduct/',seller_view.addProduct,name='addProduct'),
    url(r'^productAction/',seller_view.productAction,name='productAction'),
    url(r'^viewProduct/',seller_view.viewProduct,name='viewProduct'),
    url(r'^updateProduct/(?P<pid>\d+)/$',seller_view.updateProduct,name='updateProduct'),
    url(r'^updateAction/',seller_view.updateAction ,name='updateAction'),
    url(r'^deleteProduct/(?P<pid>\d+)/$',seller_view.deleteProduct ,name='deleteProduct'),
    url(r'^viewproducts/',buyer_view.viewproducts ,name='viewproducts'),
    url(r'^addtocart/(?P<prid>\d+)/$',buyer_view.addtocart ,name='addtocart'),
    url(r'^cartAction/',buyer_view.cartAction ,name='cartAction'),
    url(r'^viewcart/',buyer_view.viewcart ,name='viewcart'),
    url(r'^viewcart/',buyer_view.viewcart ,name='viewcart'),
    url(r'^viewSellers/',admin_view.viewSellers ,name='viewSellers'),
    url(r'^approve/(?P<sid>\d+)/$',admin_view.approve,name='approve'),
    url(r'^reject/(?P<sid>\d+)/$',admin_view.reject,name='reject'),
    url(r'^remove/(?P<cid>\d+)/$',buyer_view.remove,name='remove'),
    url(r'^confirm/(?P<oid>\d+)/$',buyer_view.confirm ,name='confirm'),
    url(r'^vieworders/',buyer_view.vieworders ,name='vieworders'),
    url(r'^cancel/(?P<caid>\d+)/$',buyer_view.cancel,name='cancel'),
    url(r'^vieworder/',seller_view.vieworder,name='vieworder'),
    url(r'^approves/(?P<cid>\d+)/$',seller_view.approves,name='approves'),
    url(r'^rejects/(?P<rid>\d+)/$',seller_view.rejects ,name='rejects'),
    url(r'^verifycancel/(?P<rid>\d+)/$',seller_view.verifycancel,name='verifycancel'),
    url(r'^addtrackingdetails/(?P<order_id>\d+)/$',seller_view.addtrackingdetails,name='addtrackingdetails'),
    url(r'^trackAction/',seller_view.trackAction,name='trackAction'),
    url(r'^viewtrackingdetails/(?P<tid>\d+)/$',buyer_view.viewtrackingdetails,name='viewtrackingdetails'),
    url(r'^productSearch/',buyer_view.productSearch ,name='productSearch'),
    url(r'^searchbyprice/',buyer_view.searchbyprice ,name='searchbyprice'),
    url(r'^priceAction/',buyer_view.priceAction ,name='priceAction'),
    url(r'^viewprofile/',buyer_view.viewprofile ,name='viewprofile'),
    url(r'^profileAction/',buyer_view.profileAction,name='profileAction'),
    url(r'^updateSeller/',seller_view.updateSeller,name='updateSeller'),
    url(r'^sellerAction/',seller_view.sellerAction,name='sellerAction'),
    url(r'^logout/',admin_view.logout,name='logout'),
    url(r'^forgottenpassword/',buyer_view.forgottenpassword,name='forgottenpassword'),
    url(r'^passwordAction/',buyer_view.passwordAction,name='passwordAction'),
    url(r'^checkDetails/',buyer_view.checkDetails,name='checkDetails'),
    url(r'^passwordUpdate/',buyer_view.passwordUpdate,name='passwordUpdate'),
   
   




    
    
    
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

