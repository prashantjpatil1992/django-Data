from django.db import models

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
    django_khalid = models.ForeignKey(Django_Khalid, on_delete=models.CASCADE)