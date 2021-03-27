from django.contrib import admin

#First import the models that you want managed in admin
from .models import Post

# Register your models here.
admin.site.register(Post)