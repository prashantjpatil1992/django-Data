from django.shortcuts import render
from .models import Table1

# Create your views here.
def Orm(request):
  # a = Table1.objects.all()
  # a = Table1.objects.all()[:2] #it work like  A LIMIT KEYWORD IN MYSQL
  # a = Table1.objects.get(id=4)
  # a = Table1.objects.exclude(id=4)
  # a = Table1.objects.filter(name='Prsahant')
  # a = Table1.objects.filter(name__icontains='Zaby')
  # a = Table1.objects.filter(name__icontains='bhai')
  # a = Table1.objects.filter(name__startswith='Pra')
  # a = Table1.objects.filter(name__endswith='ant')
  # a = Table1.objects.filter(name__exact='zaby bhai')
  # a = Table1.objects.filter(age__exact=26)
  
  # a = Table1.objects.filter(salary__gt=80000)
  # a = Table1.objects.filter(salary__lte=99000)
  # a = Table1.objects.create(name='sagar',age=16,city="Diva",salary=120000)
  # a.save()
  # a = Table1.objects.get(id=7)
  # a.delete()
  
  # a = Table1.objects.filter(id__in=[1,2,3])
  # a.delete()
  
  # a = Table1.objects.filter(pk=5).update(name='Rohan', city='Panvel')
  a = Table1.objects.filter(pk=6).update(name='Pratham', city='Badlapur')
  
  return render (request,'orm1.html',{'data':a})  