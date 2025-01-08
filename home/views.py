from django.shortcuts import render
from .models import Blogs,Category


# Create your views here.

def homePage(request):
    categories=Category.objects.all()
    featured_post=Blogs.objects.filter(is_featured=True)
    #print(featured_post)
    context={
        'categories':categories,
        'featured_post':featured_post
    }
    return render(request,'home.html',context)
    

