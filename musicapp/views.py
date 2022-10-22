from django.http import HttpResponse
from django.shortcuts import render
from .models import Abount #imported for use here

# Create your views here.
#define whateever you wish to be rendered here

def index(request):
    about1 = Abount() #instantiating the class
    about1.id = 1
    about1.name = "Stone"
    about1.details = "A 3D designer turned Cloud/DevOps Engineer. I love helping organizations save cost and time by focusing more on their business logics, less on infrastructure management, minimize errors through task automation using Continuous Integration and Continuous Deployment – CICD pipeline. I recently developed and automated the deployment of a microservice CRUD web application that lets users share images to their feed."
    
    # context = { #this will b gotten from our db later
    #     'name': 'Stone',
    #     'age': '28',
    #     'nationality': 'Nigerian'
    # }
    return render(request, 'index.html', {'about': about1}) #include ',context' to the return when you uncomment the context dictionary abv


def counter(request):
    text = request.POST['text'] #form mthod is POST(it could GET), 'text'-the name we are giving to textarea
    word_count = len(text.split()) #counts the number of words frm user captured and stored in 'text' variable
    
    return render(request, 'counter.html', {'amount': word_count}) #use the key 'amount' in the counter.html file

