from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Public

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Police').exists():
                return redirect('police_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    # Your home view logic here
    if request.user.groups.filter(name='Public').exists():
        try:
            public_profile = Public.objects.get(user=request.user)
            return render(request, 'home.html')
        except Public.DoesNotExist:
            return redirect('profile')
    else:
        return render(request, 'home.html')

@login_required(login_url='login')
def police_dashboard(request):
    # Your police dashboard view logic here
    return render(request, 'police_dashboard.html')

def profile(request):
    if request.method == 'POST':
        # Handle saving the profile details here
        return redirect('home')
    return render(request, 'profile.html')



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

def public_emergence(request):
    context={}
    return render(request,'public_emergence.html',context)

def result(request):
    context={}
    return render(request,'result.html',context)

from django.http import JsonResponse

def predict_crime_group(request):
    if request.method == 'POST':
        unit_name = request.POST.get('unitName')
        district_name = request.POST.get('districtName')
        crime_head_name = request.POST.get('crimeHeadName')
        
        # Use your ML model to predict the crime group based on the input data
        predicted_crime_group = predict(unit_name, district_name, crime_head_name)  # Implement your prediction function
        
        return JsonResponse({'crimeGroup': predicted_crime_group})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def show_result(request):
    unit_name = "Sample Unit"  # Replace with actual input value
    district_name = "Sample District"  # Replace with actual input value
    crime_head_name = "Sample Crime Head"  # Replace with actual input value
    predicted_crime_group = "Sample Predicted Crime Group"  # Replace with actual predicted value
    
    context = {
        'unit_name': unit_name,
        'district_name': district_name,
        'crime_head_name': crime_head_name,
        'predicted_crime_group': predicted_crime_group,
    }
    
    return render(request, 'result.html', context)

