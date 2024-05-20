from django.db import models
from django.contrib.auth.models import User
import random

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = random.choice(['default1.png', 'default2.png', 'default3.png', 'default4.png', 'default5.png']), upload_to='profilePics')

    def __str__(self) : return f'{self.user.username} profile' 
