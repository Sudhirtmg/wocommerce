from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import *

class UserRegisterForm(UserCreationForm):
   first_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"first name"}))
   second_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"second name"}))
   username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}))
   email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"email"}))
   bio=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"bio"}))
   password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password"}))
   password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"confirm password"}))

  
   class Meta:
        model=User
        fields=['first_name','second_name','username','email','bio']