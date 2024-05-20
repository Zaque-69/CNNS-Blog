from django.db import models
from django.contrib.auth.models import User
import random
 
class Profile(models.Model):
    icon_list = ['default_icon/default1.png', 'default_icon/default2.png', 'default_icon/default3.png', 
        'default_icon/default4.png', 'default_icon/default5.png', 'default_icon/default6.png']

    background_list = ['default_background/default1.png', 'default_background/default2.png', 'default_background/default3.png', 
        'default_background/default4.png', 'default_background/default5.png', 'default_background/default6.png']
    
    random_number = random.randint(0, 5)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    website = models.TextField( blank=True, null=True )
    description = models.TextField( blank=True, null=True )
    image = models.ImageField( blank=True, null=True, default = icon_list[random_number], upload_to='profilePics')
    background = models.ImageField( blank=True, null=True, default = background_list[random_number], upload_to='backgroundPics' )

    def __str__(self) : return f'{self.user.username} profile' 
