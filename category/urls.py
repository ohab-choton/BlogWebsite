from django.urls import path
from . import views


urlpatterns = [
   path('blogs/<int:category_id>/', views.categoryPage ,name='categoryPage'),
   

]