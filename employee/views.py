from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from.forms import UserCreationForm
# Create your views here.
 


def index(request):
    
    return render(request, 'employee/index.html')
 


def loginEmployee(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method=='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user=User.objects.get(username=username)
        except: 
            messages.error(request, 'Username does not exist')
            
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'index') 
        else:
            messages.error(request, 'Username or password does not exist')
            
    return render(request, 'employee/login_register.html')



def logoutEmployee(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('login')


def registerEmployee(request):   
    page = 'register'
    if request.user.is_authenticated:
        return redirect('index') 
    form= UserCreationForm()
    
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, "Account created!")
            
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Error occurred during registration")
    context={'page':page, 'form':form}
    return render(request, 'employee/login_register.html', context)