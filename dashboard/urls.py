from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboardPage ,name='dashboardPage'),
    path('category_1/', views.category_1 ,name='category_1'),
]

