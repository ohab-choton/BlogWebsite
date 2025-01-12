from django.shortcuts import render
from .models import Blogs,Category
from django.http import HttpResponse


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




    

