from django.urls import path
from . import views\

app_name='petadmin'

urlpatterns = [
    path('login' , views.a_login, name= 'login') ,
    path('homepage' , views.a_homepage, name= 'homepage'),
    path('viewseller' , views.a_vuseller, name= 'viewseller'),
    path('apprv/<int:sid>' , views.approve, name= 'apprv'),
    path('sellers' , views.a_sellers, name= 'sellers')
]
