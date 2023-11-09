from django.urls import path
from myapp import views


urlpatterns = [
     path('home/',views.home,name='home'),
     path('enter/',views.data,name="enter"),
     path('update/<int:id>',views.update,name="update"),
     path('<int:id>',views.Delete,name="delete"),
     path('cart/',views.cart, name="cart"),
     path('addtocart/',views.add_to_cart,name='addtocart'),
     path('viewcart/',views.view_cart)
]
