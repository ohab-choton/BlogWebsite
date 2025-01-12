from django.shortcuts import render,redirect
from .models import Blogs,Category
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

def homePage(request):
    categories=Category.objects.all()
    featured_post=Blogs.objects.filter(is_featured=True,status=1)
    posts=Blogs.objects.filter(is_featured=False,status=1)
    print(posts)
    
    context={
        'categories':categories,
        'featured_post':featured_post,
        'posts':posts

    }
    return render(request,'home.html',context)


#register
def registerPage(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registerPage')
    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'register.html',context)

#login
def loginPage(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('homePage')
    form=AuthenticationForm()
    context={
        'form':form
    }

    return render(request,'login.html',context)
#logout page
def logoutPage(request):
    auth.logout(request)
    return redirect('homePage')





    

