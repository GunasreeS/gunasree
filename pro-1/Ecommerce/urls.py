from django.urls import path
from Ecommerce import views
from django.contrib.auth import views as v


urlpatterns = [
    path('',views.home,name="hm"),
    ##path('log/',views.login,name="log"),
    path('reg/',views.registration,name="reg"),
    path('cnt/',views.contactus,name="ct"),
    path('dash/',views.dashboard,name="dsh"),
    path('lg/',v.LoginView.as_view(template_name="html/login.html"),name="lg"),
    path('pro/',views.profile,name='prof'),
    path('lgo/',v.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
    path('updt/',views.updpf,name="updpf"),
]