# MUSICAPP USING DJANGO

## Create a virtual environment

- Create a virtual environment by running the command, `mkdir <project_name>` to create project folder
- cd into the project folder `cd <project_folder>`
- run `virtualenv <env_name>` to create environment
cd into the environment and run `<env_name>\Scripts\activate` to activate the virtual environment

## Install django in the environment
- run the command, `pip install django` to install django
- You can run, `django-admin --version` to check the installation

## Creating Django project
- run the command, `django-admin startproject <project_name>` to create a django project
- a new folder with the name you have choosen will have appeared in the project directory
- cd into the project directory
To start server run the command, `python manage.py runserver`.

## Creating the *musicapp* application
- run the command, `python manage.py startapp <your_app_name`. remember the server has to be running
- add the *~musicapp~* to the list of installed app in settings.py
To access the admin endpoint, magration has to be applied.
- run the command, `python manage.py migrate` to apply migration.
- go to *~<ip_address:port/admin>~* to access the login page.

To create a user
- run the command, `python manage.py createsuperuser`
Follow the prompt to provide *~username~*, *~email_address~* and *~password~*.
The credentials can then be used to login to the ***musicapp*** admin page.

## Create **requirements.txt** file
While your virtualenv is active, run `pip freeze > requirements.txt`. This will generate a .txt file with the list of packages required to run this project.
- to install the requirement.txt contents run, `pip install -r requirement.txt`

## Configure urls and render views
- Open the musicapp/urls.py and create url path to be rendered by the view
- add the path, *~path('', views.index, name="index")~* to the 'urlpatterns' list
- goto ***views.py*** file and create your view. In my case, I simply returned an HttpResponse
- goto into songcrud/urls.py and update it to render our musicapp view
- import *~include~* 
- then do, ***path('', include('musicapp.urls'))***
- save and refresh the homepage.

## Creating Custom Template files
- create a folder *templates* in the root directory
- go to setting.py and add directory to the templates in the *TEMPLATES* list. i.e do, `BASE_DIR, 'templates'` in the DIRS list
- in the *templates* folder, create your *index.html* file
- in *views.py*, you do `return render(request, 'index.html')`

## Sending Dynamic Data to Your Template File
- in your function definition in views.py file, you could include a dictionary to represent data from database
- the keys can then be used in the index.html file using *{{key}}*

## Building a Word Counter In Django
- firs is to create a form tag with input space and a submit button in our index.html file
- give it a POST method
### Sending the content to another url
- include *action="counter"* to the form tag, also include a 'POST' method.
- go to the *urls.py* and include another path with the action name above
- goto the *views.py* and create a function named *counter* that returns *counter.html*
- then in the *templates* folder create an html file named *counter.html* 
- now when a user inputs words in form pg, it the data will be sent the path /counter
- to extract this data, go to views.py and create a variable 'text' which u assigned to the 'textarea' tag and use *len(text.split())* count the number of words
- since it's a 'POST' mthd, django requires a *CSRF* token to verify this.
- To achieve this, go to index.html file and include, `{% csrf_token %}` in the form tag
- refresh the webpage, input texts and click 'submit' this should work fine

## Static Files in Django
This refers to any external file such as a css, img, video files that is linking to our html files in the template folde.
- create a new folder named *static* in the base directory. this will contain all the static files
- to tell django where to find these static files, go the settings.py file in your django project named *songcrud* here
- at the top do, `import os`.
- below 'STATIC_URL' do, ` STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
- in the static folder, create a css file, *style.css*.
- go to the index.html file and link the css file using the link tag.
- in the same file do , `{% load static %}` to load the file
- refresh your home page to view changes

## Linking Static File from Bootstrap
Download HTML template on bootstrapmade.com
- move the file to your django project dir

