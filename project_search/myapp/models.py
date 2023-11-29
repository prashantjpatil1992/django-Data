from django.db import models

# Create your models here.

class Products(models.Model):
  pname = models.CharField(max_length=100, null=True)
  price = models.PositiveBigIntegerField(null=True)
  quantity = models.PositiveBigIntegerField(null=True)
  about = models.CharField(max_length=100, null=True)
  
  def __str__(self):
    return self.pname
