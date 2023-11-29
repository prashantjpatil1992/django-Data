from django.shortcuts import render
from .models import Products
from django.db.models import Q

# Create your views here.
def Index(request):
  if request.method == "POST":
    search = request.POST.get('search')
    all = Products.objects.all()
    print(all.values_list('pname',flat=True))
    
    os = Products.objects.filter(Q(pname__icontains=search) | Q(price__icontains=search)| Q(quantity__icontains=search)| Q(about__icontains=search))
     
  else:
    os = Products.objects.all()
  return render(request, 'index.html',{'data':os})