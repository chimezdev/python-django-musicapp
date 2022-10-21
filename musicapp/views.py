from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#define whateever you wish to be rendered here
def index(request):
    return HttpResponse('<h1>Hey, Welcome to my MusicApp</h1>')