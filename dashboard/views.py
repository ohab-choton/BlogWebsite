from django.shortcuts import render
from home.models import Category,Blogs
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='loginPage')
def dashboardPage(request):
    categories = Category.objects.all()

    categories_count=Category.objects.all().count()
    blogs_count=Blogs.objects.all().count()

    context = {
        'categories': categories,
        'categories_count':categories_count,
        'blogs_count':blogs_count,
        }
    return render(request,'dashboard.html',context) 

def category_1(request):
    categories = Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,'category1.html',context)