from django.shortcuts import render

from .models import Post

# Create your views here.

def test_view(request):
  return render(request, "homepage.html")

def greet_view(request, name):
  data = {}
  data["username"] = name
  return render(request, 'greet.html', context=data)

def list_posts(request):
  data = {}
  posts = Post.objects.filter(status=1).order_by('-created_on')
  data['post_list'] = posts

  return render(request, "post_list.html", context=data)

## The old way of doing things
# from django.http import HttpResponse


# def test_view(request):
#   name = "abdulwahab"
#   return HttpResponse(f"""
#   <html>
#   <head>

#   </head>
#     <body>
#       <h2>hello {name}!</h2>

#       <p>
#       This is our <strong>first</strong> web application!
#       </p>

#     </body>
#   </html>
#   """)
