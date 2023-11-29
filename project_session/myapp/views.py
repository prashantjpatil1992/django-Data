from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.

def SetSession(request):
  request.session['username'] = 'rahul123'
  # request.session.flush()
  request.session.set_expiry(30)
  return HttpResponse('Session has been set')

def GetSession(request):
  try:
    if request.session['username']:
      uname = request.session['username']
      return HttpResponse(f'your username is {uname}')
  except:
    return HttpResponse('Session Time Out')
   
    

def Login(request):
  
  if request.method == "POST":
    uname = request.POST.get('uname')
    print(uname)
    request.session['username1'] = uname
    request.session.set_expiry(30)
     
    return HttpResponseRedirect('/profile/')
  a = request.session['username1']
  return render(request, 'login.html', {'a':a})

def Profile(request):
  try:
    if request.session['username1']:
      a = request.session['username1']
        # request.session.flush()
      return render(request, 'profile.html',{'a':a})
  # else:
  #   return HttpResponseRedirect('/login/')
  except:
    return HttpResponseRedirect('/login/')
  # return render(request, 'profile.html')
  
# def logout(request):
#   if request.session['username1']:
#    
#     return HttpResponseRedirect('/login/')

#   return HttpResponse('logout')
    



