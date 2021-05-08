from django.urls import path
from App import views
from django.contrib.auth import views as v

urlpatterns =[
    path('store/',views.store,name="store"),
    path('',views.home,name="home"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('Payment/',views.payment,name="pay"),
    path('product/',views.product,name="product"),
    path('lg/',v.LoginView.as_view(template_name="html/login.html"),name="lg"),
    path('reg/',views.registration,name="reg"),

]