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

## Creating Template files
- create a folder *templates* in the root directory
- go to setting.py and add directory to the templates in the *TEMPLATES* list
- in the *templates* folder, create your *index.html* file
- in views.py, you can instead return render