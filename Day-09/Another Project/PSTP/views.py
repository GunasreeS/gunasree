from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'ht/homepage.html')


def chk(request):
	return HttpResponse("<script>alert('Hi Good Afternoon')</script><h2>Welcome</h2>")

def homepage(request):
	return render(request,'ht/homepage.html')

def lgn(re):
	return render(re,'ht/login.html')

def reg(rt):
	return render(rt,'ht/register.html')

def bthm(qw):
	return render(qw,'ht/bthome.html')
def about(req):
	return render(req,'ht/about.html')

def contact(req):
	return render(req,'ht/contact.html')