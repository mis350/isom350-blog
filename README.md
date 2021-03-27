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

# 3- Admin - Changes
1. Create an admin user by running the following command in shell then follow instructions:
```bash
python manage.py createsuperuser
```

2. Register any model you want the admin to control in blog/admin.py. See the file to learn how to register a model to be controled by the admin

3. Run the django server by hittin run in replit, then open the application website and add the path /admin to the url to go to the admin site. Login using the admin user you created from step 1 and you can start managing posts.

# 4- Improved admin - Changes
1. Changes made in admins.py that allows us to control how the post is managed in the admin interface. See the changes made in blog/admin.py

# 5- Views - Changes
1. Add PostListView to list posts in blog/views.py
2. Add PostView to show a detailed view of the post in blog/views.py

# 6- urls - Changes
1. create blog/urls.py
2. update mysite/urls.py to include blog/urls.py

# 7- Templates - Changes
1. Created templates directory under blog app directory
2. created post_list.html and post_detail.html under blog/templates

# 8- Linked Templates - Changes
1. linking post list to detailed blog in post_list.html using url tag
2. add link back to list from detailed view using url tag
3. use truncatewords filter on blog body to create summary in post_list template
4. use timesince filter to display relative time for blog post list in post_list template

# 9- Improve Design - Changes
1. created a templates directory in the root directory of the proejct and added the base.html that will be used to style all the pages in the website.
2. Updated setting.py to let Django know where to find the base template by updating **TEMPLATES** configuration by changing the **DIR** value, it should look like this:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # only this line was changed
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
3. Updated post_list.html and post_detail.html templates to extend base.html, where base.html utilizes bootstrap framework for creating responsive ui.


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

