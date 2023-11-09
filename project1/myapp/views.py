from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World !")

def about(ll):
    name = "ABC"
    age = 40
    data = f"{name}, {age}"
    return HttpResponse(data)


def aa(request):
    a = [1,2,3,4]
    for i in a:
        print(i)
    b =f"{a[0]} \n {a[1]} \n {a[2]}"
    return HttpResponse(b)