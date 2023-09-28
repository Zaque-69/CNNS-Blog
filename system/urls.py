from django.urls import path
from . import views
from .views import PostListView, PostdDetailView, PostCreateView, PostUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('error/', views.error, name = 'errorLog'),
    path('post/new/', PostCreateView.as_view(), name = 'post-new'),
    path('register/', views.register, name = 'register'),
    path('login/', views.loginSystem, name = 'log'),
    path('profile/',  views.profile , name = 'profile'),
    path('post/<pk>/', PostdDetailView.as_view(), name = 'post-detail'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    #path('post/<pk>/delete', PostdeleteView.as_view(), name = 'post-delete'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html') , name = 'logout'),
    path('contact/', views.contactPage, name = 'contactPage')
]
