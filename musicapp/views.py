from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#define whateever you wish to be rendered here

def index(request):
    context = { #this will b gotten from our db later
        'name': 'Stone',
        'age': '28',
        'nationality': 'Nigerian'
    }
    return render(request, 'index.html', context) #include ',context' to the return when you uncomment the context dictionary abv


def counter(request):
    text = request.POST['text'] #form mthod is POST(it could GET), 'text'-the name we are giving to textarea
    word_count = len(text.split()) #counts the number of words frm user captured and stored in 'text' variable
    
    return render(request, 'counter.html', {'amount': word_count}) #use the key 'amount' in the counter.html file

