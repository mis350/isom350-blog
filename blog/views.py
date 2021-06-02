import datetime

from django.shortcuts import render, get_object_or_404

from .models import Post


# using render (the right way)
def test_view(request):
  return render(request, 'ahmed.html')

def greet_view(request, name):
  data = {}
  data["greeted"] = name
  return render(request, 'greet.html', context=data)

def list_posts_view(request):
  
  # we want all posts before may 1st 2021
  # compare_date = datetime.datetime.now()
  #(2021, 5, 1)
  #data_list = Post.objects.filter(created_on__lt=compare_date)

  # we want all posts after may 1st 2021
  #data_list = Post.objects.filter(created_on__lt=compare_date)

  # We want all posts between may 1st and June 1st

  start_date = datetime.datetime(2021, 5, 1)
  end_date = datetime.datetime(2021, 6, 1)
  data_list = Post.objects.filter(created_on__range=(start_date, end_date))
  data = {}
  data["posts"] = data_list
  return render(request, "post_list.html", context=data)


def post_search(request, q):
  data_list = Post.objects.filter(title__icontains=q)
  data = {}
  data["posts"] = data_list
  return render(request, "post_list.html", context=data)


def post_details(request, s):
  #obj = Post.objects.get(slug=s)
  obj = get_object_or_404(Post, slug=s)

  comments = obj.comment_set.all()

  data = {}
  data["post"] = obj
  data["comments"] = comments
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
