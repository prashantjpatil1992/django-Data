from django.shortcuts import render,HttpResponse

# Create your views here.
def home2(request):
    return HttpResponse('Hello From App2')
