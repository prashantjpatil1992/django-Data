from django.contrib import admin
from .models import Persons, Cars, Teacher, Student

# Register your models here.
admin.site.register(Persons)
admin.site.register(Cars)
admin.site.register(Teacher)
admin.site.register(Student)