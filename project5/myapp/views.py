from django.shortcuts import render,HttpResponseRedirect
from .models import Django_Khalid, Cart,Order
from .forms import django_form, SignUp_Form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def home(request):
    a = Django_Khalid.objects.all()
    return render(request,'index.html',{'data':a})

def data(request):
    if request.method == "POST":
        fm = django_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm = django_form()
            messages.success(request,"Data Added Successfully...")
            return HttpResponseRedirect('/main/home/')
    else:
        fm = django_form()
    return render(request,'data_enter.html',{'form':fm})


def update(request,id):
    if request.method == "POST":
        pi = Django_Khalid.objects.get(pk=id)
        fm = django_form(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Data Deleted Successfully...")
            return HttpResponseRedirect('/main/home/')
    else:
        pi = Django_Khalid.objects.get(pk=id)
        fm = django_form(instance=pi)
    return render(request,'update.html',{'form':fm})

def Delete(request,id):
    if request.method=="POST":
        pi = Django_Khalid.objects.get(pk=id)
        pi.delete()
        messages.success(request,"Data Deleted Successfully...")
        return HttpResponseRedirect('/main/home/')
    
    
def cart(request):
    if request.user.is_authenticated:
        print(request.user)
        a = Django_Khalid.objects.all()
        cart1 = Cart.objects.filter(user=request.user)
        count = cart1.count()
        return render (request, 'cart.html',{'data':a, 'cartcount':count})
    else:
        return HttpResponseRedirect('/main/login/')

def add_to_cart(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            
            item,store = Cart.objects.get_or_create(django_khalid_id=cid,user=request.user)
            print(item,store)
            
            if not store:
                item.quantity += 1
                item.save()
            
            return HttpResponseRedirect('/main/cart/')
        
def cart_increse(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            
            item,store = Cart.objects.get_or_create(django_khalid_id=cid)
            print(item,store)
            if not store:
                item.quantity += 1
                item.save()
                return HttpResponseRedirect('/main/viewcart/')
        
def cart_decrese(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            
            item,store = Cart.objects.get_or_create(django_khalid_id=cid)
            print(item,store)
            if not store:
                item.quantity -= 1
                item.save()
                if item.quantity < 1:
                    item.delete()
            
                
                return HttpResponseRedirect('/main/viewcart/')
        
def view_cart(request):
    if request.user.is_authenticated:
        
        
        # cart1 = Cart.objects.all().values_list('django_khalid_id', flat=True)
        # cartdata = Django_Khalid.objects.filter(id__in=cart1)
        # print(cart1)
        cart1 = Cart.objects.filter(user=request.user).values_list('django_khalid_id',flat=True)
        cartdata = Django_Khalid.objects.filter(id__in=cart1)
        print(cart1)
        print(request.user)
        quantity = Cart.objects.all()
    
        # print(quantity.values_list('quantity',flat=True))
        
        return render(request, 'show cart.html',{'data':cartdata,'quantity':quantity})
    else:
        return HttpResponseRedirect('/main/login/')

def remove_cart(request,id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            os = Cart.objects.filter(django_khalid_id=id)
            os.delete()
            return HttpResponseRedirect('/main/viewcart/')
    
def SignUp(request):
    if request.method == "POST":
        fm = SignUp_Form(request.POST)
        if fm.is_valid():
            print(fm)
            fm.save()
            fm = SignUp_Form()
    else:
        fm = SignUp_Form()
    return render(request,'signup.html',{'form':fm})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/main/cart/')
        
    return render(request,'login.html')

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/main/login/')


def Order_Place(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_id = request.POST.get('pid')
            cart_id = request.POST.get('cid')
            print(product_id)
            Order.objects.create(user=request.user,django_khalid_id=product_id,cart_id=cart_id)
            return HttpResponseRedirect('/main/ordermessage/')
            
def view_order(request):
    order = Order.objects.all().values_list('django_khalid_id',flat=True)
    data = Django_Khalid.objects.filter(id__in=order)
    return render(request, 'view_order.html',{'data':data})
 
def Order_message(request):
    return render(request,'order_message.html')


        

