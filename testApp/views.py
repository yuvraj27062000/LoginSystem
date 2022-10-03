from django.shortcuts import render,redirect
from testApp import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"mainfolder/home.html")

@login_required
def python(request):
    return render(request,"mainfolder/python.html")

@login_required
def java(request):
    return render(request,"mainfolder/java.html")

@login_required
def aptitute(request):
    return render(request,"mainfolder/aptitute.html")

def logout(request):
    return render(request,"mainfolder/logout.html")

def signup(request):  
    form=forms.SignupForm()
    if request.method=='POST': 
        form=forms.SignupForm(request.POST) 
        print('form')
        if form.is_valid():
            user=form.save() 
            user.set_password(user.password) 
            user.save()
            print('save') 
            redirect('/accounts/login') 
    return render(request,'mainfolder/signup.html',{'form':form}) 