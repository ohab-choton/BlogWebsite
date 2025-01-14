from django import forms
from home.models import Category,Blogs

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields= '__all__'

class BlogsForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields= ('title','category','author' ,'blog_image','short_description','blog_body', 'status', 'is_featured') 
