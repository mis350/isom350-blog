
from django.urls import path
from . import views

urlpatterns = [
  path('test/', views.test_view), 
  path('tajroba/', views.test_view),
  path('tt/', views.test_view), 
  path('greet/<str:name>/', views.greet_view),
  path('posts/', views.list_posts_view),
]