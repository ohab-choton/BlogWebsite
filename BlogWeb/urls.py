"""
URL configuration for BlogWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from category import views as blogsVies
from home import views as homeVies

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('category/',include('category.urls')),
    path('blog/search/',blogsVies.search ,name='search'),
    path('register/',homeVies.registerPage ,name='registerPage'),
    path('login/',homeVies.loginPage ,name='loginPage'),
    path('logout/',homeVies.logoutPage ,name='logoutPage'),
    path('dashboard/',include('dashboard.urls')),
       
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



