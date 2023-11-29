from django.shortcuts import render
from .models import Courses

# Create your views here.
def Home(request):
  os = Courses.objects.all()
  return render(request,'home.html', {'url':os})

def Courses1(request,slug):
  os = Courses.objects.filter(slug=slug)
  print(os)
  return render(request,'courses.html',{'data':os})