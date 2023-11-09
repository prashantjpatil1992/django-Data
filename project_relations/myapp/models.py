from django.db import models

# Create your models here.

class Persons(models.Model):
  name = models.CharField(max_length=100, null=True)
  city = models.CharField(max_length=100, null=True)
  phone = models.PositiveBigIntegerField(null=True)
  
  def __str__(self):
    return self.name
  
class Cars(models.Model):
  carname = models.CharField(max_length=100, null=True)
  person = models.ForeignKey(Persons, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.carname} {self.person}"
  
  
class Teacher(models.Model):
  tname = models.CharField(max_length=100)
  
  def __str__(self):
    return self.tname
  
class Student(models.Model):
  sname = models.CharField(max_length=100)
  tname = models.ManyToManyField(Teacher)
  
  def __str__(self):
    return f"{self.sname} {self.tname}"
  
  