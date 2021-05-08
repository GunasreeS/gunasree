from Emp.models import UsrRg
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields = ['username','email','password']
		widgets = {
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Username",
			"required":True,
			}),
		"password":forms.PasswordInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Password",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email id",
			"required":True,
			}),
		}