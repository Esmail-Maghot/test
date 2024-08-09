from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature 


# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features':features} )

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']

        if password == repeat_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,"This Email is already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"This Username is already used")
                return redirect('register')
            else:
                user =User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password is not the same ")
            return redirect('register')
                
    else:
        return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password )
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Credentials invalid")
            return redirect('login')
    else:
        return render(request, 'Login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')

def post(request,pk):
    return render(request,'post.html', {'pk':pk})

def counter(request):
    posts = [1, 2, 3, 4, 5, 'Tom', 'Tim', 'Bob']
    return render(request,'counter.html', {'posts':posts})