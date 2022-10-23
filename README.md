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
- move the index.html file to the template folder
- move the asset folder to the static folder
- open the index.html file and link it the way django recognizes it
- do `{% load static %}` at the topmost, this tells django to load the file
- edit all the 'href="" by including {% %} to enclose its contents btw the "".
- press and hold 'alt' and select multiple


## Intro to Django Models
In django models are mostly used in configuring our database
Often times in django you don't have to write SQL code to get your db running
Remember 'Model(used for db) View(how it is presented to the user) Template(html)
From model, we pass our data to the template
we use classes in python to build our db
- open the models.py in the musicapp dir
- create a class About with id, name and details
Next is to use this in our views
- goto the views.py file and import the class
- in the index function in views.py, and instantiate the class 'About'
- in the 'index.html', replace the <p> content with {{about.details}}
- to make the div tag dynamic, you can do to loop over it with `{{% for abt in about %}}`
- the conditional statement could also be used within the index.html file, just write the python code in between {% %}

## Django Admin Panel and Manipulation of Database
lets make the data in the models.py real data for the db
django uses sqlite as its default db
- go to the models.py file, to convert the class to b a model for our db:
- open a pair of bracket after the class name and do (models.Model).
- id attr is no longer needed, our db automatically adds that
- rewrite the name attr in this format, `name = models.CharField(max_length=50)`
- repeat for 'details' field but parameter 'max_length=500'
For the model to be saved to our db, you need to migrate it by running these two commands in our terminal
- if you have not added your app to the list of installed app in the settings.py, it is necessary to do so to be able to integrate the db of your app.
- run `python manage.py makemigrations`(tells python to save any changes in the models file) and prepare it for migration
- run `python manage.py migrate` (sends the changes to the db)
- **Repeat the above two steps anytime you make changes to your models file**
The above migrates our data to the sqlite db. To view, and manage it, we go to the addmin route.
- login to it with the 'superuser' created at the begining of this project or run, `python manage.py createsuperuser`

# Django Admin login(Authentication in Django)
django has admin part
The admin.py controls this therefore, we need to register our models there so that data from the models can appear in the admin url.
- in the *admin.py* import the class About which is now a model.
- add this line of code, `admin.site.register(About)`
- refreshing the page will show that a new table named about has been added.
- click on **+Add** to add data to the table
- an about object will be instantiated with the attributes you provided.
- back to the 'views.py' file, instead of providing the objects there manually, we can use the data from our db.
- to access the data in db, import 'About' from models
- in the function index, add a new variable to store the data received by doing, `about = About.objects.all()`
- refreshing the homepage, will print the code block we looped in d index.html the number of times the About object in our db.

