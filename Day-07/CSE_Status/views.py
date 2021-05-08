from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
	return HttpResponse("Happy Holi")

def sd(req):
	return HttpResponse("Good Afternoon")

def dtye(request,ru):
	return HttpResponse("Hello "+ru)

def ref(qr,age,name):
	return HttpResponse("Your Name is: {}</br>Your age is: {}".format(name,age))

def recrd(ax,sal,name,age,state):
	return HttpResponse("<h2>Your Name is: <span style='background-color:black;color:white'>{}</span></h2><h3>Your age is: <span style='background-color:green;color:white'>{}</span></h3><h4 style='background-color:magenta;color:white'>Your Salary is: {}</h4><h5>Your State is: {}</h5>".format(name,age,sal,state))

