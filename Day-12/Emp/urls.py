from django.urls import path
from Emp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('log/',views.login,name="lg"),
	path('reg/',views.registration,name="rg"),
	path('cr/',views.crud,name="cd"),
	path('delt/<str:id>',views.deletedata,name="delete"),
]