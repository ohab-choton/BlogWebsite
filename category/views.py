from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from home.models import Blogs ,Category

# Create your views here.
def categoryPage(request,category_id):
    #fetch the posts that belogns to the category with id category_id
    posts=Blogs.objects.filter(status=1,category=category_id)
    categories = Category.objects.all()
    
    # when don't find the categoryid jus go back homepage
    try:
        category=Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return redirect('homePage')
    context={
        'posts':posts,
        'category':category,
        'categories':categories,
    }
    return render(request, 'category.html',context)



#this is for slug when you visit with slug , then show with categories
def blogs(request, slug):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'blogs.html', context)


   
   