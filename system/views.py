import json
from .models import Post, Comment
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UpdateUser, UpdateUserAfterClass
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html', {
        'posts' : Post.objects.all().order_by('-date_posted'),
        'comments' : Comment.objects.all()
    })

def clasaX(request):
    return render(request, 'clasaX.html', {
        'posts' : Post.objects.all().order_by('-date_posted')
    })

def error(request) : 
    return render(request, '404.html')

def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        form.save()
        usern = request.POST.get('username')
        passw = request.POST.get('password1')
        user = authenticate(request, username = usern, password = passw)
        login(request, user)
        return redirect('ClassRoom')
    
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
        #else : messages.info(request, "Three credits remain in your account.")

    return render(request, 'login.html')


def SelectClass(request):
    form = UpdateUserAfterClass()
    listOfCodes = ["HKKnGCU3LJv5f3rd1TUrPQ==", "JahLB6ny+in3NYZq/6qyGQ==",
                       "cc5MScnZUesxuthyWo52iQ==", "pbWhFEPPPbjWSxoLpYhSqg=="]
    if request.method == 'POST':
        ok = 0
        form = UpdateUserAfterClass(request.POST, instance = request.user)
        for code in listOfCodes :
            requestInvitation = request.POST.get('last_name')
            if code == requestInvitation : ok = 1

        if ok == 1 : 
            print(json.loads)
            if form.is_valid() : 
                with open("./system/static/js/main.json", "r") as f: 
                    requestInvitation = json.load(f)[requestInvitation]
                print(requestInvitation)
                form.save()
            return redirect('home')
        #else : messages.info(request, "Three credits remain in your account.")

    return render(request, 'classroom.html', {
        'form' : form
    })


@login_required
def profile(request):
    u_profile = UpdateUser()
    if request.method == 'POST' :
        u_profile = UpdateUser(request.POST, instance = request.user)
        if u_profile.is_valid() : 
            u_profile.save()
    return render(request, 'profile.html', { 'u_form' : u_profile,})


def StatusCode404(request, exception):
    return render(request, '404.html')

@login_required
def contactPage(request) : 
    return render(request, 'contact.html')

@login_required
def anunturiPage(request) : 
    return render(request, 'anunturi.html', {
        'posts' : Post.objects.all().order_by('-date_posted')
    })

@login_required
def comentarii(request) : 
    return render(request, 'comment.html')



class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostdDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'postNew.html'
    fields = ['title', 'content', 'class4post', 'image']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'postNew.html'
    fields = ['title', 'content', 'class4post', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author : return True
        else : return False


class PostdeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'postDelete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author : return True
        else : return False

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'postNewComment.html'
    fields = ['post', 'body', 'class4post']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostdDetailViewComment(DetailView):
    model = Comment
    template_name = 'post_detail.html'

class PostUpdateViewComment(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'postNewComment.html'
    fields = ['post', 'body', 'class4post']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author : return True
        else : return False

class PostdeleteViewComment(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'postDelete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author : return True
        else : return False
