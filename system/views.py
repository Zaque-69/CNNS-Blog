from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UpdateUser
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostdDetailView(DeleteView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'postNew.html'
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'postNew.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author : return True
        else : return False

'''class PostdeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    template_name = 'postDelete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author : return True
        else : return False'''

def error(request) : return render(request, '404.html')

def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('log')
        else : return redirect('errorLog')

    return render(request, 'register.html', {
        'form' : form
        })

def loginSystem(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password1')
        user = authenticate(request, username = usern, password = passw)

        if user is not None : 
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

@login_required
def profile(request):
    u_profile = UpdateUser()

    if request.method == 'POST' :
        u_profile = UpdateUser(request.POST, instance = request.user)
        
        if u_profile.is_valid() : 
            u_profile.save()

    context = {
        'u_form' : u_profile,
    }
    return render(request, 'profile.html', context)

'''def delete_post(request, id):
    post_to_delete=Post.objects.get(id = object.id)
    post_to_delete.delete()'''

def StatusCode404(request, exception):
    return render(request, '404.html')
