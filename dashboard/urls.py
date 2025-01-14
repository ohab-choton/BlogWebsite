from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.dashboardPage ,name='dashboardPage'),
    path('category_1/', views.category_1 ,name='category_1Page'),
    path('category_1/add',views.addCategory,name='addCategoryPage'),
    path('category_1/edit/<int:pk>',views.editCategory,name='editCategoryPage'),
    path('category_1/delete/<int:pk>',views.deleteCategory,name='deleteCategoryPage'),

    path('posts/',views.posts,name='postsPage'),
    path('posts/add',views.addPost,name='addPostPage'),
    path('posts/edit/<int:pk>',views.editPost,name='editPostPage'),
    path('posts/delete/<int:pk>',views.deletePost,name='deletePostPage'),

    path('user/',views.userPage,name='userPage'),
    path('user/add',views.addUser,name='addUserPage'),


]

