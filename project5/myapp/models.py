from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

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
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    order_id = models.CharField(max_length=100,null=True, unique=True)
    
    def save(self,*args,**kwargs):
        if not self.order_id:
            current_time = timezone.now()
            order_id = f"{current_time.strftime('%Y%d%m%H%M%S')}-{uuid.uuid4().hex[:5]}"
            self.order_id = order_id
        super().save(*args,**kwargs)
    
