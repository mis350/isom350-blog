import datetime

from django.shortcuts import render

from .models import Post

# using render (the right way)
def test_view(request):
  return render(request, 'ahmed.html')

def greet_view(request, name):
  data = {}
  data["greeted"] = name
  return render(request, 'greet.html', context=data)

def list_posts_view(request):
  d1 = datetime.datetime(2021, 5, 1)
  d2 = datetime.datetime(2021, 6, 1)

  data_list = Post.objects.filter(created_on__range=(d1, d2))


  data = {}
  data["posts"] = data_list
  return render(request, "post_list.html", context=data)


def search_posts_view(request, query):

  data_list = Post.objects.filter(title__icontains=query)

  data = {}
  data["posts"] = data_list
  return render(request, "post_list.html", context=data)


def detailed_post_view(request, s):
  obj = Post.objects.get(slug=s)
  
  comment_list = obj.comment_set.all()

  data = {
    "post": obj,
    "comments": comment_list,
  }
  return render(request, "post_detail.html", context=data)

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
