from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    class4post = models.CharField(max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self) : return reverse('post-detail', kwargs = {'pk' : self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments', on_delete=models.CASCADE)
    body = models.TextField()
    class4post = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) : return self.post.title

    def get_absolute_url(self) : return reverse('comments-detail', kwargs = {'pk' : self.pk})

class ImageModel(models.Model):
    title = models.CharField(max_length=255)
    class4post = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profilePics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) : return self.title

    def get_absolute_url(self) : return reverse('image-detail', kwargs = {'pk' : self.pk})
