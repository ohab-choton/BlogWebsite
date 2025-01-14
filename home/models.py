from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

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

    def save(self, *args, **kwargs):
        # Only set slug if it's not already set
        if not self.slug:  
            words = self.title.split()[:5]  
            # Create a slug
            self.slug = slugify(' '.join(words))  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title 
    
class Comments(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        blog=models.ForeignKey(Blogs,on_delete=models.CASCADE)
        comment=models.TextField(max_length=100)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.comment

 
