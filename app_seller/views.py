from django.shortcuts import render, redirect
from . models import Signup, Productss
from rest_framework.response import Response


# Create your views here.
def login(request):

    if request.method == 'POST':
        
        email = request.POST['usrname']
        password = request.POST['pswd']

        # print(email)
        # print(password)
        
        try:
            userObj = Signup.objects.get(username=email,password=password)
            
            if userObj.status=='approved':
                request.session['logged_user'] = userObj.id
                return redirect('app_seller:homepage')
            else:
                return render (request, 'app_seller/login.html',{'errMsg':'approval pending'})
           
        except Exception as e:
            print(e)
            return render (request, 'app_seller/login.html',{'errMsg':'LoginFailed'})

    return render(request, 'app_seller/login.html')

def addproduct(request):
    
    if request.method=='POST':
        prdname = request.POST['pname']
        category = request.POST['catgry']
        brand = request.POST['pbrand']
        price = request.POST['pprice']
        qntty = request.POST['qnty']
        discount = request.POST['disprice']
        weight = request.POST['weyt']
        image = request.FILES['img']
        descrptn = request.POST['descr']

        addobj = Productss(product_name = prdname , category=category , product_brand=brand , product_price=price , quantity=qntty , discount_price=discount ,weight=weight , product_image=image , description=descrptn)
        addobj.save()
    return render(request, 'app_seller/addproduct.html')


def register(request):

    if request.method=='POST':
        frstname = request.POST['fname']
        scndname = request.POST['sname']
        phnnmbr = request.POST['phone']
        username = request.POST['uname']
        password = request.POST['pswd']
        accntname = request.POST['aname']
        accntnmbr = request.POST['anumbr']
        ifsc = request.POST['ifsc']


        signupobj = Signup(first_name = frstname , second_name = scndname , phone_number = phnnmbr , username = username , password = password ,account_name = accntname , account_number = accntnmbr, ifsc_code = ifsc)
        signupobj.save()
        # c_dta=Signup.objects.get(username=username,password=password)
        # c_id=c_dta.id

        # return render(request, 'app_seller/registration.html',{'c_id':c_id})
        
    return render(request, 'app_seller/registration.html')



def home(request):
    return render(request, 'app_seller/homepage.html')

def profile(request):
    if 'logged_user' in request.session:
        userObj = Signup.objects.get(id=request.session['logged_user'])
        return render(request, 'app_seller/profile.html', {'currentUser':userObj})
    
    
    return render(request,'app_seller/profile.html')

def products(request):
    
    userobj = Productss.objects.all()
    
    return render(request,'app_seller/products.html', {'prddet':userobj})


def frontend(request):
        response = request.get('http://127.0.0.1:8000/sample/load_student')
        data = response.json()
        return render(request,'app_seller/frontend_api.html', {'data': data})
