from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Post
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'home.html', context)

def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'register.html', {
        'form' : form
        })

def loginSystem(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password1')
        user = authenticate(request, username = usern, password = passw)

        #try:
        #if user is not None : 
        login(request, user)
        return redirect('home')
        #except AttributeError : print('ma-ta')

    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
