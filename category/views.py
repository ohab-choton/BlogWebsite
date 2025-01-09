from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *

# Create your views here.
def categoryPage(request,category_id):
    #fetch the posts that belogns to the category with id category_id
    posts=Blogs.objects.filter(status=1,category=category_id)
    
    # when don't find the categoryid jus go back homepage
    try:
        category=Category.objects.get(pk=category_id)
    except:
        return redirect('homePage')
    context={
        'posts':posts,
        'category':category

    }
    return render(request, 'category.html',context)
   
   