from django import forms
from home.models import Category,Blogs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields= '__all__'

class BlogsForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields= ('title','category','author' ,'blog_image','short_description','blog_body', 'status', 'is_featured') 

class AdduserForm(forms.ModelForm):
    class Meta:
        model=User
        fields= ('first_name','last_name','username','email','password' ,'is_staff','is_superuser','is_active','groups','user_permissions')
