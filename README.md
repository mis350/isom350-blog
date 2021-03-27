# 1-Setup - Changes
1. create app 'blog' using
```bash
python manage.py startapp blog
```
2. In the files mysite/settings.py, add the blog app to list of INSTALLED_APPS. It should look like this:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

# 2- Models - Changes
1. Create the database models in **blog/models.py** to reflect the data requirements of the project (typically visualized using the ER-Diagram). 

2. Prepare the data definition files for the used database by typing in shell:
```bash
python manage.py makemigrations
```
**Note:** You run this command everytime a change is made to the models

3. Create the database tables by running the following in shell:
```bash
python manage.py migrate
```
**Note:** You run this command everytime after running makemigrations


# Developing Django on Repl.it

- Fork this template to get started
- Simply hit run to start the server
- The server will autoreload as needed. You don't need to restart the server manually.

## Add your first view

1. Create a file under `mysite` named `views.py` with the following contents:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

2. Add a url pattern under `mysite/urls.py`. It should look like this:

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
```

## Shell

Django utilizes the shell for managing your site. For this click on the `?` in the lower-right corner and click "Workspace shortcuts" from there you can open a new shell pane. 

## Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

