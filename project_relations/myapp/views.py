from django.shortcuts import render
from .models import Persons, Cars

# Create your views here.
def index(request):
  os1 = Persons.objects.all()
  os12 = Cars.objects.all()
  os1 = list(os1)
  os12 = list(os12)
  od = os1 + os12
  print(od)
  
  return render(request, 'index.html', {'person':od})
