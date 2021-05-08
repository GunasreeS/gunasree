from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def login(request):
	return render(request,'html/login.html')

def registration(request):
	if request.method == "POST":
		u = request.POST['uname']
		p = request.POST['pd']
		m = request.POST['eml']
		a = request.POST['ag']
		d = {'us':u,'em':m,'age':a,"ps":p}
		return render(request,'html/details.html',d)
	return render(request,'html/register.html') 