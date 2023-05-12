from django.urls import path
from . import views
app_name = "app_customer"

urlpatterns = [  
     path('login' , views.login, name= 'login'),
     path('dashboard' , views.dashboard, name= 'dashboard'),
     path('register' , views.register, name= 'register'),
     path('home' , views.homepage, name= 'home'),
     path('shop_by_dog' , views.shopdog, name= 'shopdog'),
     path('shop_by_cat' , views.shopcat, name= 'shopcat'),
      path('shop_by_smallpets' , views.shopsmallpets, name= 'shopsmallpets'),
     path('brands' , views.brands, name='brands'),
     path('view_products' , views.viewproducts, name='products')



]
