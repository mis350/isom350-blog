import datetime

from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post

from .forms import PostForm, CommentForm

def test_view(request): #1
    data = {} #2
    data["my_name"] = "Mohammad" #3
    return render(request, "hello_world.html", context=data) #4

# using render (the right way)
# def test_view(request):
#   return render(request, 'ahmed.html')

def greet_view(request, name):
  data = {}
  data["greeted"] = name
  return render(request, 'greet.html', context=data)

def list_posts_view(request):
  
  # # d = datetime.datetime(2021, 4,1)
  # # data_list = Post.objects.filter(created_on__gt=d)

  # d1 = datetime.datetime(2021, 5, 1)
  # d2 = datetime.datetime(2021, 6, 1)

  # data_list = Post.objects.filter(created_on__range=(d1, d2))
  data_list = Post.objects.all()

  data = {}
  data["posts"] = data_list
  return render(request, "post_list.html", context=data)

def search_posts(request, query):
  data_list = Post.objects.filter(title__icontains=query)
  data = {}
  data["posts"] = data_list
  return render(request, "post_list.html", context=data)


def show_post(request, s):
  obj = Post.objects.get(slug=s)
  comments = obj.comment_set.all()

  data = {}
  data["post"] = obj
  data["comment_list"] = comments
  
  f = CommentForm(request.POST or None, initial={
    "post": obj.id,
  })
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect('show-post', s=obj.slug)
  return render(request, "post_detail.html", context=data)


def create_post(request):
  form = PostForm(request.POST or None)

  data = {}
  data["form"] = form

  if form.is_valid():
    post = form.save(commit=False)
    post.slug = slugify(post.title)
    post.save()
    #return redirect("list-posts")
    return redirect("show-post", s=post.slug)

  return render(request, "create_post.html", context=data)


def edit_post(request, s):
  p = get_object_or_404(Post, slug=s)
  f = PostForm(request.POST or None, instance=p)

  data = {}
  data["post"] = p
  data["form"] = f

  if f.is_valid():
    post = f.save(commit=False)
    post.slug = slugify(post.title)
    post.save()
    return redirect("show-post", s=post.slug)
  return render(request, "edit_post.html", context=data)


def delete_post(request, s):
  p = get_object_or_404(Post, slug=s)

  m = f"Do you want to delete {p.title}?"
  data = {
    "message": m,
  }
  
  if "confirm" in request.GET:
    p.delete()
    return redirect("list-posts")
  elif "cancel" in request.GET:
    return redirect("list-posts")
  else:
    return render(request, "confirm.html", context=data)
  
# This is the not so right way
# from django.http import HttpResponse

# # Create your views here.
# def test_view(request):
#   name = "jawaher"
#   return HttpResponse(f'''
#   <html>
#     <body>
    
#     <h2>hello {name}!</h2>

#   <p>
#   this is my <strong>first</strong> web app!
#   </p>

#   <p>
#   this is the second line
#   </p>

#     </body>
#   </html>
#   ''')
