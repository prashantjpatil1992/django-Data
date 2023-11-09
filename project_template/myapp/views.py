from django.shortcuts import render
from .models import Temaplate
from .forms import FormForm
from django.contrib import messages

# Create your views here.

def Base(request):
  if request.method == "POST":
    name1 = request.POST.get('name')
    age1 = request.POST.get('age')
    
    data = Temaplate.objects.create(name=name1,age=age1)
    data.save()
    
  return render (request,'base.html')


def Form(request):
  if request.method == "GET":
    name1 = request.GET.get('name')
    age1 = request.GET.get('age')
    data = Temaplate.objects.create(name=name1,age=age1)
    messages.success(request,"Data Submitted in Table Successfully...")
    data.save()

    fm = FormForm()
    os = Temaplate.objects.all()
  else:
    os = Temaplate.objects.all()
    fm = FormForm()
  return render (request,'forms.html', {'form':fm, 'data':os})

def Condi(request):
  a = {'value':22,'value1':33,'value2':[1,2,3,'abc','xyz'], 'value3':{'name':'abc','age':23}}
  return render(request,'condition.html',a)


def Loop(request):
  a = {'value':['khalid','siddiqui','sagar','zaby bhai','rohan sir'],'value1':{'name':'ABC','age':23,'city':'Thane'}}
  return render(request,'loop.html',a)