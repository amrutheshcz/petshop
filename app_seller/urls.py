from django.urls import path
from . import views
app_name = "app_seller"
urlpatterns = [

    path('login' , views.login, name= 'login'),
    path('addproduct' , views.addproduct, name= 'addproduct'),
    path('registration' , views.register, name= 'register'),
    path('homepage' , views.home, name= 'homepage'),
    path('profile' , views.profile, name= 'profile'),
    path('products' , views.products, name= 'products'),
    path('frontend' , views.frontend, name= 'frontendapi')
    
]