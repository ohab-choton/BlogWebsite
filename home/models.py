from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

STATUS_CHOICES=(
    (0,'Draft'),
    (1,'Publish')
)

class Blogs(models.Model):
    title=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_image=models.ImageField(upload_to='uploads/%y/%m/%d/')
    short_description=models.TextField(max_length=2000)
    blog_body=models.TextField(max_length=3000)
    status=models.IntegerField(choices=STATUS_CHOICES,default=0)
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

 
