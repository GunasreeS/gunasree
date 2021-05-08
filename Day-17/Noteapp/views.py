from django.shortcuts import render,redirect
from Noteapp.forms import UsForm,ComplaintForm,ImForm,UtupForm
from django.core.mail import send_mail
from NoteSharing import settings
from django.contrib import messages
from django.contrib.auth.models import User
from Noteapp.models import ImProfile
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
def profile(req):
	d=ImForm()
	return render(req,'stc/profile.html',{'d':d})

def complaint(req):
	if req.method=="POST":
		data=ComplaintForm(req.POST)
		if data.is_valid():
			subject='Confirmation_complaint'
			body="thank you for complaint"+req.POST['p_name']
			receiver=req.POST['p_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			data.save()
			messages.success(req,"Successfully sent to your mail "+receiver)
			return redirect('/')
	form=ComplaintForm()
	return render(req,'stc/complaint.html',{'c':form})


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
	return render(request,'stc/updateprofile.html',{'us':u,"imp":i})