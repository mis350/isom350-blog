from django.urls import path

from .views import test_view, greet_view, list_posts

urlpatterns = [
    path('test/', test_view),
    path('mashael/', test_view),
    # path('', test_view),
    path('greet/<str:name>/', greet_view),
    path('posts/', list_posts),
]

