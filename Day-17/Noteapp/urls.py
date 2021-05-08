from django.urls import path
from Noteapp import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('pro/',views.profile,name="profile"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="cn"),
	path('lg/',ad.LoginView.as_view(template_name='stc/login.html'),name="log"),
	path('rg/',views.regi,name="rge"),
	path('ds/',views.dashboard,name="dsh"),
	path('lgo/',ad.LogoutView.as_view(template_name='stc/logout.html'),name="logo"),
    path('comp/',views.complaint,name="cp"),
    path('updf/',views.updpf,name="upf"),
    ]