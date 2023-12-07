from django.contrib import admin
from .models import Django_Khalid,Cart,Order

# Register your models here.
@admin.register(Django_Khalid)
class admin1(admin.ModelAdmin):
    display_list = ['name','age']
    
    def __str__(self):
        return self.name
    
admin.site.register(Cart)
admin.site.register(Order)