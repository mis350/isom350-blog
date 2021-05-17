from django.shortcuts import render

# Create your views here.

def test_view(request):
  return render(request, "homepage.html")



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
