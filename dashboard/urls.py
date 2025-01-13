from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboardPage ,name='dashboardPage'),
]

