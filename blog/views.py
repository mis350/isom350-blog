from django.shortcuts import render

# using render (the right way)
def test_view(request):
  return render(request, 'ahmed.html')

def greet_view(request, name):
  data = {}
  data["greeted"] = name
  return render(request, 'greet.html', context=data)

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
