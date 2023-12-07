from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in,sender=User)
def beginning(sender,request,user,**kwargs):
  print("******************")
  print("User Login Successfully......")
  
# user_logged_in.connect(beginning,sender=User)

@receiver(user_logged_out,sender=User)
def the_end(sender,request,user,**kwargs):
  print("****************")
  print("Log Out Successfully.....")
  print("****************")

# user_logged_out.connect(the_end,sender=User)


@receiver(user_login_failed)
def error(sender,credentials,**kwargs):
  print("Username or password not match...")
  print("Login failed")
  
@receiver(pre_save,sender=User)
def before_save(sender,instance,**kwrags):
  print("***************")
  print("You are entering data into the User table")
  print("Will save soon....")
  
