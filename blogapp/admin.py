from django.contrib import admin

from blogapp.models import Comment, Like, Post, PostView

from .models import Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)
