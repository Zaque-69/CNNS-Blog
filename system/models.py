from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100,blank=True, null = True,)
    class4post = models.CharField(max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.TextField(blank=True, null = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self) : return reverse('post-detail', kwargs = {'pk' : self.pk})

class Comment(models.Model):
    idComment = models.CharField(max_length=100)
    body = models.TextField()
    class4post = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.TextField(blank=True, null = True)
    #ImageField(blank=True, null=True, upload_to='commentsImages')

    def __str__(self) : return self.idComment
    
    def get_absolute_url(self) : return reverse('comments-detail', kwargs = {'pk' : self.pk})
