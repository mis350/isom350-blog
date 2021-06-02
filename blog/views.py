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
  
  data_list = Post.objects.filter(
    created_on__month=3,
    created_on__day=2,
    created_on__hour=17,
    created_on__year=2019,
    )

  data = {}
  data["posts"] = data_list
  return render(request, "post_list.html", context=data)

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
