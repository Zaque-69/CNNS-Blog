from django.contrib import admin
from .models import Post, Comment, ImageModel

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ImageModel)

#admin.site.register(Profile)
