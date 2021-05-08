from django.db import models

# Create your models here.

class UsrRg(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	age = models.IntegerField(default=10)

	def __str__(self):
		return self.username+" "+self.email

class NewData(models.Model):
	ch = [
	('M','Male'),('F','Female')
	]
	mobile = models.IntegerField(default=9875845789)
	gender = models.CharField(max_length=10,choices=ch)
	pid = models.OneToOneField(UsrRg,on_delete=models.CASCADE)