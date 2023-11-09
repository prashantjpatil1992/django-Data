from django.db import models

# Create your models here.
class Table1(models.Model):
  name = models.CharField(max_length=255,null=True)
  age = models.IntegerField(null=True)
  salary = models.FloatField(null=True)
  city = models.CharField(max_length=200,null=True)
  
  
class ID(models.Model):
  id_number = models.CharField(max_length=100, null=True)
  
  def __str__(self):
    return self.id_number

class Person(models.Model):
  name = models.CharField(max_length=100, null=True)
  age = models.IntegerField(null=True)
  city = models.CharField(max_length=100,null=True)
  ID = models.OneToOneField(ID, on_delete=models.CASCADE, null=True)
   
  def __str__(self):
    return self.name
  

  
  
