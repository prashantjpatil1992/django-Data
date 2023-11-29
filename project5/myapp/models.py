from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Django_Khalid(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField(upload_to='Images',null=True,blank=True)
    time = models.TimeField(auto_now_add=True, null=True)
    gender = models.CharField(max_length=40, default=False)
    English = models.BooleanField(default=False)
    Hindi = models.BooleanField(default=False)
    Marathi = models.BooleanField(default=False)
    city = models.CharField(max_length=100, default=False)
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    django_khalid = models.ForeignKey(Django_Khalid, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,null=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    django_khalid = models.ForeignKey(Django_Khalid, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    order_id = models.PositiveBigIntegerField(default=1234, null=True)
    
