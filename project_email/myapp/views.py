from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# def Email(request):
#   subject = 'Test Mail'
#   message = 'Thank You For Provinding Your Email To Test Our Application'
#   mail_from = settings.EMAIL_HOST_USER
#   recipient_list = ['singhpratham520@gmail.com','bangarprathmesh.3636@gmail.com','rachananaik13@gmail.com','rohanpatilandu@gmail.com','sjchavan2014@gmail.com','kzabiullah191@gmail.com','piyush124@gmail.com']
  
#   send_mail(subject,message,mail_from,recipient_list)
#   return HttpResponse('Mail Sended To All')

def Sign_up(request):
  if request.method == "GET":
    username = request.GET.get('uname')
    first_name = request.GET.get('fname')
    last_name = request.GET.get('lname')
    email = request.GET.get('email')
    print(username,first_name,last_name,email)
    try:
      subject = f"Welcome To Goa {first_name} {last_name}"
      message = f"""
      This mail is just for to inform you that you are the member of Goa team mr {username}
      
      please do not reply this is auto genrated mail
      """
      mail_from = settings.EMAIL_HOST_USER
      recipient_list = [f"{email}"]
      send_mail(subject, message, mail_from,recipient_list, fail_silently=False)
      return render(request,'sign_up.html')
    except:
      return render(request,'sign_up.html')


