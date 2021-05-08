from django.shortcuts import render,redirect
from Noteapp.forms import UsForm

# Create your views here.

def home(request):
	return render(request,'stc/home.html')

def about(request):
	return render(request,'stc/about.html')

def contact(request):
	return render(request,'stc/contact.html')

def regi(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsForm()
	return render(request,'stc/register.html',{'u':p})

def dashboard(request):
	return render(request,'stc/dashboard.html')
