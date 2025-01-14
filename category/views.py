from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from home.models import Blogs ,Category,Comments
from django.db.models import Q
from django.http import HttpResponseRedirect

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
    single_post=get_object_or_404(Blogs,slug=slug,status=1)
    ##comments
    if request.method=='POST':
        comment=Comments()
        comment.user=request.user
        comment.blog=single_post
        # blogs.html textarea name is 'comment'
        comment.comment=request.POST.get('comment')
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments=Comments.objects.filter(blog=single_post)
    comment_count=comments.count()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'single_post': single_post,
        'comments':comments,
        'comment_count':comment_count
    }
    return render(request, 'blogs.html', context)


#search
def search(request):
    categories = Category.objects.all()
    
    keyword=request.GET.get('keyword')
    blogs=Blogs.objects.filter(Q(title__icontains=keyword) | Q(blog_body__icontains=keyword) | Q(short_description__icontains=keyword) )
    content={
        'blogs':blogs,
        'categories':categories,
        'keyword':keyword
    }

    return render(request,'search.html',content)


   
   