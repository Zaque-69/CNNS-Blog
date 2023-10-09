from django.urls import path
from . import views
from .views import (PostdDetailView, PostCreateView,
                    PostUpdateView, PostdeleteView,
                    PostUpdateViewComment, PostdeleteViewComment,
                    PostdDetailViewComment,CommentCreateView, 
                    ImageCreateView,ImageUpdateView, 
                    ImageDeleteView, ImageDetailView)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('error/', views.error, name = 'errorLog'),
    path('register/', views.register, name = 'register'),
    path('login/', views.loginSystem, name = 'log'),
    path('profile/',  views.profile , name = 'profile'),

    path('post/new/', PostCreateView.as_view(), name = 'post-new'),
    path('post/<pk>/', PostdDetailView.as_view(), name = 'post-detail'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<pk>/delete/', PostdeleteView.as_view(), name = 'post-delete'),

    path('comment/new/', CommentCreateView.as_view(), name = 'comment-new'),
    path('comment/<pk>/', PostdDetailViewComment.as_view(), name = 'comments-detail'),
    path('comment/<pk>/update/', PostUpdateViewComment.as_view(), name = 'comments-update'),
    path('comment/<pk>/delete/', PostdeleteViewComment.as_view(), name = 'comments-delete'),

    path('image/new/', ImageCreateView.as_view(), name = 'image-new'),
    path('image/<pk>/', ImageDetailView.as_view(), name = 'image-detail'),
    path('image/<pk>/update/', ImageUpdateView.as_view(), name = 'image-update'),
    path('image/<pk>/delete/', ImageDeleteView.as_view(), name = 'image-delete'),

    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html') , name = 'logout'),
    path('contact/', views.contactPage, name = 'contactPage'),
    path('clasaX/', views.clasaX, name = 'clasaX'),
    path('classroom/', views.SelectClass, name = 'ClassRoom'),
    path('anunturi/', views.anunturiPage, name = 'anunturi'),
]
