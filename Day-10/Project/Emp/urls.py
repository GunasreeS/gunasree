from django.urls import path
from Emp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('log/',views.login,name="lg"),
]