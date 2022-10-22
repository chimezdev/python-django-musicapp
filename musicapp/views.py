from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#define whateever you wish to be rendered here
def index(request):
    return render(request, 'index.html')