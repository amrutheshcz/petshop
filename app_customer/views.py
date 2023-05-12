from django.shortcuts import render


def login(request):
    return render(request, 'app_customer/login.html')

def register(request):
    return render(request, 'app_customer/register.html')

def dashboard(request):
    return render(request, 'app_customer/dashboard.html')
    

def homepage(request):
    return render(request, 'app_customer/home.html')

def shopdog(request):
    return render(request, 'app_customer/shop_by_dog.html')

def shopcat(request):
    return render(request, 'app_customer/shop_by_cat.html')

def shopsmallpets(request):
    return render(request, 'app_customer/shop_by_smallpets.html')

def brands(request):
    return render(request, 'app_customer/brands.html')

def viewproducts(request):
    return render(request, 'app_customer/view_products.html')