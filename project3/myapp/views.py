from django.shortcuts import render

# Create your views here.
def index(request):
    a=["abc","123",444,999,"lll"]
    return render(request,'index.html',{'a':a})
