from django.contrib import admin
from destination.models import BlogPost
from . import models

# Register your models here.
admin.site.register(BlogPost)



# new model for comment and review for each destination post
# new one

# class CommentAdmin(models.Comment):
#     list_display = ("post", "name", "email", "publish", "status")
#     list_filter =  ("status", "publish")
#     search_fields = ("name", "email", "content")

