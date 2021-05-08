from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from App.models import Product
from App.forms import UsForm

# Create your views here.
def home(req):
	return render(req,'html/home.html')


def store(req):
	return render(req,'html/store.html')

def cart(req):
	return render(req,'html/cart.html')

def checkout(req):
	return render(req,'html/checkout.html')

def payment(req):
	return render(req,'html/payment.html')

def product(req):
	if req.method=="POST":
		it_ty=req.POST['itemtype']
		it_na=req.POST['itemname']
		price=req.POST['price']
		if len(price)!=0:
			data=Product.objects.create(itemtype=it_ty,itemname=it_na,price=price)
			data2=Product.objects.all()
			return render(req,'html/product.html',{'info':data2})
	data2=Product.objects.all()
	return render(req,'html/product.html',{'info':data2})

def registration(req):
	if req.method=="POST":
		p=UsForm(req.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsForm()
	return render(req,'html/registration.html',{'u':p})
