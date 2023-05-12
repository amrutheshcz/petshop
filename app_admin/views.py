from django.shortcuts import render , redirect 
from  app_seller.models import Signup

# Create your views here.


def a_login(request):
    return render(request, 'app_admin/login.html')

def a_homepage(request):
    return render(request, 'app_admin/homepage.html')

def a_vuseller(request):
        
    userObj = Signup.objects.all()

    return render(request, 'app_admin/viewseller.html',{'seldet':userObj})

def approve(request, sid):
    sellobj = Signup.objects.get(id = sid)
    sellobj.status = 'approved'
    sellobj.save()
    return redirect('petadmin:viewseller')
    
def a_sellers(request):
        
    userObj = Signup.objects.all()

    return render(request, 'app_admin/sellers.html',{'seldet':userObj})

