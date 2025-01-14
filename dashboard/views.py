from django.shortcuts import render,redirect
from home.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from . forms import CategoryForm,BlogsForm
from django.shortcuts import get_object_or_404



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
    return render(request,'dashbord/dashboard.html',context) 

def category_1(request):
    categories = Category.objects.all()

    context={
        'categories':categories
    }
    return render(request,'dashbord/category1.html',context)

#add category
def addCategory(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashbord/category_1Page')
            
    form=CategoryForm()
    categories = Category.objects.all()
    context={
        'categories':categories,
        'form':form
    }
    return render(request,'dashbord/addCategory.html',context)

#edit category
def editCategory(request,pk):
    cat=get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=cat)
        if form.is_valid():
            form.save()
            return redirect('dashbord/category_1Page')
        
    form=CategoryForm( instance=cat) 
    
    context={
        'form':form,
        'cat':cat
    }
    return render(request,'dashbord/editCategory.html',context)

#delete category
def deleteCategory(request,pk):
    cat=get_object_or_404(Category,pk=pk)
    cat.delete()

    return redirect('dashbord/category_1Page')

#posts page
def posts(request):
    posts=Blogs.objects.all()
    categories=Category.objects.all()
    context= {
        'categories':categories,
        'posts':posts,
        }
    return render(request,'dashbord/posts.html',context)

#add_post
def addPost(request):
    if request.method=='POST':
        form=BlogsForm(request.POST,request.FILES) # request.FILES use for upload image
        if form.is_valid():
            form.save()
            print("success")
            return redirect('postsPage')
        
        else:
            print(form.errors)
    post=Blogs.objects.all()
    categories=Category.objects.all()
    form= BlogsForm()
   
    context= {'post':post,'categories':categories,'form':form}
    
    return render (request , 'dashbord/addPost.html',context )


          
  