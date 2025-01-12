from django.urls import path
from . import views
from category import views as blogsVies

urlpatterns = [

    path('', views.homePage ,name='homePage'),
    path('blogs/<slug:slug>/',blogsVies.blogs,name='blogs'),
   
    
    
]