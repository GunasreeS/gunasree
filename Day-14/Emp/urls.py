from django.urls import path
from Emp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('log/',views.login,name="lg"),
	path('reg/',views.registration,name="rg"),
	path('cr/',views.crud,name="cd"),
	path('delt/<int:st>/',views.deletedata,name="delete"),
	path('df/',views.dform,name="dff"),
	path('showdata/',views.showinfo,name="show"),
	path('infodelete/<int:et>',views.infodelete,name='infodelete'),
	# path('edit/<int:id>',views.edit,name="editdata"),
	path('e/<int:si>/',views.userupdate,name="ue"),


]