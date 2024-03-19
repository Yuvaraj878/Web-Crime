from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Police').exists():
                return redirect('police_dashboard')  # Redirect to police dashboard if police user
            else:
                return redirect('home')  # Redirect to home for regular users
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    username = request.user.username
    return render(request, 'home.html', {'username': username})

@login_required(login_url='login')
def police_dashboard(request):
    # Only police users will reach here due to login_required decorator and user authentication check in user_login view
    return render(request, 'police_dashboard.html')


def profile(request):
    context={}
    return render(request,'profile.html',context)

def home(request):
    context={}
    return render(request,'home.html',context)

def dashboard(request):
    context={}
    return render(request,'dashboard.html',context)

def emergency(request):
    context={}
    return render(request,'emergency.html',context)

def complient(request):
    context={}
    return render(request,'complient.html',context)


def police_dashboard(request):
    context={}
    return render(request,'police_dashboard.html',context)
