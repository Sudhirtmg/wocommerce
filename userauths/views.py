from django.shortcuts import render,redirect
from userauths.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def signup(rq):
    form=UserRegisterForm()

    if rq.method=='POST':
        form=UserRegisterForm(rq.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(rq,f'{username},was created successfully')
            return redirect('signin')
            
    else:
            form=UserRegisterForm()
    context={
        'form':form
    }
            
    return render(rq,'auth/signup.html',context)

def signin(rq):
 if rq.user.is_authenticated:
     return redirect('index')
 else:
    if rq.method=='POST':
        username=rq.POST.get('username')
        password=rq.POST.get('password')

        user=authenticate(rq,username=username,password=password)
        if user is not None:
            login(rq,user)
            messages.success(rq,'you are logged in')
            return redirect('index')
        else:
            messages.error(rq,'not logged in')
 return render(rq,'auth/signin.html')
 
def logout_view(rq):
    logout(rq)
    messages.success(rq,'logged out')

    return redirect('signin')
          
     
          
     
