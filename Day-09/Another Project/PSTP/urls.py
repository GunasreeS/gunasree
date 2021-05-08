from django.urls import path
from PSTP import views

urlpatterns = [
	path('rt/',views.home,name="home"),
	path('demo/',views.chk),
	path('hm/',views.homepage),
	path('lg/',views.lgn),
	path('rg/',views.reg,name="register"),
	path('',views.bthm),
	path('about/',views.about,name="about"),
	path('contact/',views.contact,name="contact"),
]