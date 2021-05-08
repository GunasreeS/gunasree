from django.shortcuts import render,redirect
from Ecommerce.forms import UsForm,UtupForm,ImForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from Ecommercesite import settings
from django.contrib import messages
from django.contrib.auth.models import User 
from Ecommerce.models import Improfile

# Create your views here.
def home(req):
	return render(req,'html/home.html')

def contactus(req):
	return render(req,'html/contactus.html')

def registration(req):
	if req.method=="POST":
		p=UsForm(req.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsForm()
	return render(req,'html/registration.html',{'u':p})
@login_required
def dashboard(req):
	return render(req,'html/dashboard.html')

@login_required
def profile(req):
	d=ImForm()
	return render(req,'html/profile.html')

@login_required
def updpf(request):
	if request.method == "POST":
		u=UtupForm(request.POST,instance=request.user)
		i=ImForm(request.POST,request.FILES,instance=request.user.improfile)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/pro')
	u=UtupForm(instance=request.user)
	i=ImForm(instance=request.user.improfile)
	return render(request,'html/updateprofile.html',{'us':u,'imp':i})
