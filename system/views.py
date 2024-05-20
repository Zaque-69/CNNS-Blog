from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Post, Comment
from users.forms import ProfileIconForm
from .forms import UserRegistrationForm, UpdateUser, UpdateUserAfterClass
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def contactPage(request) : 
    return render(request, 'contact.html')

@login_required
def comentarii(request) : 
    return render(request, 'comment.html')

@login_required
def home(request): 
    return render(request, 'home.html', {
        'posts' : Post.objects.all().order_by('-date_posted'),
        'comments' : Comment.objects.all().order_by('-date_posted')
    })
 
@login_required
def clasaX(request):
    return render(request, 'clasaX.html', {
        'posts' : Post.objects.all().order_by('-date_posted'),
        'comments' : Comment.objects.all().order_by('-date_posted')
    })

@login_required
def profile(request):
    return render(request, 'profile.html', {
        'posts' : Post.objects.all().order_by('-date_posted'),
        'comments' : Comment.objects.all().order_by('-date_posted')
    })

@login_required
def clasa_mea(request):
    return render(request, 'clasa_mea.html', {
        'posts' : Post.objects.all().order_by('-date_posted'),
        'comments' : Comment.objects.all().order_by('-date_posted')
    })

@login_required
def anunturiPage(request) : 
    return render(request, 'anunturi.html', {
        'posts' : Post.objects.all().order_by('-date_posted'),
        'comments' : Comment.objects.all().order_by('-date_posted')
    })

def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        try : 
            form.save()
        except : 
            pass

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
    listOfCodes = ["mxWLOPyckongDCJGBpQK", "eRstQPMlfBoYsLBVZgMW",
                    "QFdINEQehJkVrcHZtUJs", "amcYvyDjbIjNAWyLEwJG",
                    'RQRYehryuCqGGvTCJpek', "postare_normala"]
    if request.method == 'POST':
        ok = 0
        form = UpdateUserAfterClass(request.POST, instance = request.user)
        for code in listOfCodes :
            requestInvitation = request.POST.get('last_name')
            if code == requestInvitation : ok = 1

        if ok == 1 : 
            if form.is_valid() : 
                form.save()
                return redirect('home')
                
    return render(request, 'classroom.html', {
        'form' : form
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UpdateUser(request.POST, instance=request.user)
        p_form = ProfileIconForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UpdateUser(instance=request.user)
        p_form = ProfileIconForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })

class PostdDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = Comment.objects.filter(post=post)
        context['comments'] = comments
        return context

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
    fields = ['idComment', 'body', 'class4post', 'image']
 
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostdDetailViewComment(DetailView):
    model = Comment
    template_name = 'post_detail.html'

class PostUpdateViewComment(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'postNewComment.html'
    fields = ['idComment', 'body', 'class4post', 'image']

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

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
        'posts' : Post.objects.all().order_by('-date_posted'),
        'comments' : Comment.objects.all().order_by('-date_posted')
        }
    return render(request, 'profile.html', context)