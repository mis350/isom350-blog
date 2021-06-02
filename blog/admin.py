from django.contrib import admin

#First import the models that you want managed in admin
from .models import Post, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
  model = Comment

# The following is used to configure the admin for Post
class PostAdmin(admin.ModelAdmin):
  # Set which columns to show in the post admin list
  list_display = ('title', 'slug', 'status','created_on')

  # Which columns we can filter the posts on
  # We can choose to see draft or published posts
  list_filter = ("status",)

  # Which fields will the search work on.
  # Here we request that search is done on title and content only
  search_fields = ['title', 'content']

  # This tells the admin to create the slug based on value of the title
  # it is created automatically as we type the title without the need for us to enter the slug
  prepopulated_fields = {'slug': ('title',)}
  
  inlines = [CommentInline,]

# notice change here, we want to use the PostAdmin class
# as configuration for post administrator
admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
