from django.shortcuts import render
def login(request):
    context={}
    return render(request,'login.html',context)

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

def police_dashboard(request):
    context={}
    return render(request,'police_dashboard.html',context)