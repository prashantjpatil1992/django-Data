from django.shortcuts import render,HttpResponseRedirect
from .models import Django_Khalid, Cart
from .forms import django_form
from django.contrib import messages

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
    a = Django_Khalid.objects.all()
    cart1 = Cart.objects.all().values_list('django_khalid_id', flat=True)
    count = cart1.count()
    return render (request, 'cart.html',{'data':a, 'cartcount':count})

def add_to_cart(request):
    if request.method == "GET":
        cid = request.GET.get('cid')
        print(cid)
        item,store = Cart.objects.get_or_create(django_khalid_id=cid)
        print(item,store)
        
        if not store:
            item.quantity += 1
            item.save()
        
        return HttpResponseRedirect('/main/cart/')
    
def view_cart(request):
    cart1 = Cart.objects.all().values_list('django_khalid_id', flat=True)
    cartdata = Django_Khalid.objects.filter(id__in=cart1)
    print(cart1)
    
    quantity = Cart.objects.all()
    
    # print(quantity.values_list('quantity',flat=True))
    
    return render(request, 'show cart.html',{'data':cartdata, 'quantity':quantity})

def remove_cart(request,id):
    if request.method == 'GET':
        os = Cart.objects.filter(django_khalid_id=id)
        os.delete()
        return HttpResponseRedirect('/main/viewcart/')
        


