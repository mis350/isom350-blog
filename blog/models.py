from django.db import models

# Create your models here.
class Post(models.Model):
  # The following allows us to display status values as text
  # Notice that the status field is an integer which will be limited to the value 0 or 1
  STATUS = (
    (0,"Draft"),
    (1,"Publish")
  )

  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)

  def __str__(self):
    # This method tells django what to display when a post object is printed or what to display in the admin interface. 
    # Here we are requesting that the title only is displayed. You can return any constructed string.
    # Always use self.xxx to access instance variables
    return self.title