from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import About #imported for use here
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
#define whateever you wish to be rendered here

def index(request):
    
    about = About.objects.all();
        
    # context = { #this will b gotten from our db later
    #     'name': 'Stone',
    #     'age': '28',
    #     'nationality': 'Nigerian'
    # }
    return render(request, 'index.html', {'about': about}) #include ',context' to the return when you uncomment the context dictionary abv


def register(request):
    if request.method == 'POST': #verify and process the code block if 'POST' mthd
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2: #continue only if both passwords match
            # confirm that email doesn't exist already in our user db
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist') #returns mssg if email exist
                return redirect('register') # redirect the user to form page
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else: #creates new user with the credentials received
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save() #save the user then redirect user to login page
                return redirect('login')
        else: # if both password doesn't match return mssg
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else: #i.e if not a POST mthd just render the page
        return render(request, 'register.html')
    
    
def login(request):
    if request.method == 'POST': #check if its a 'POST' method
        username = request.POST['username'] #store the entered details
        password = request.POST['password']
        
        # authenticate user
        user = auth.authenticate(username=username, password=password)
        if user is not None: #checks if user exits in our db
            auth.login(request, user) #log the user in if exists
            return redirect('/') #then redirect user to home page
        else: 
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request) #this line logs the user out of the app
    return redirect('/') # return user to homepage


def counter(request):
    text = request.POST['text'] #form mthod is POST(it could GET), 'text'-the name we are giving to textarea
    word_count = len(text.split()) #counts the number of words frm user captured and stored in 'text' variable
    
    return render(request, 'counter.html', {'amount': word_count}) #use the key 'amount' in the counter.html file

