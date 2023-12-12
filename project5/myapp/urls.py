from django.urls import path
from myapp import views


urlpatterns = [
     path('home/',views.home,name='home'),
     path('enter/',views.data,name="enter"),
     path('update/<int:id>',views.update,name="update"),
     path('<int:id>',views.Delete,name="delete"),
     path('cart/',views.cart, name="cart"),
     path('addtocart/',views.add_to_cart,name='addtocart'),
     path('viewcart/',views.view_cart,name='viewcart'),
     path('removecart/<int:id>',views.remove_cart, name='removecart'),
     path('cartincrese/',views.cart_increse,name='cartincrese'),
     path('cartdecrese/',views.cart_decrese,name='cartdecrese'),
     path('signup/',views.SignUp, name='signup'),
     path('login/',views.Login,name='login'),
     path('logout/',views.LogOut,name='logout'),
     path('orderplace/',views.Order_Place, name='orderplace'),
     path('ordermessage/',views.Order_message, name='ordermessage'),
     path('vieworder/',views.view_order, name='vieworder'),
     path('pay/',views.Payment, name="pay")
]
