from django.db import models

# Create your models here.

class UsrRg(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	age = models.IntegerField()
