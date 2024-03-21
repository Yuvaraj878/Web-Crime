from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Public

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check for first-time login and redirect to profile if needed
            if not user.public_profile.exists():  # Leverage `exists()` for efficiency
                return redirect('profile')
            if user.groups.filter(name='Police').exists():
                return redirect('police_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


@login_required(login_url='login')
def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check if the user belongs to the 'Public' group
        if request.user.groups.filter(name='Public').exists():
            try:
                # Attempt to get the user's public profile
                profile = Public.objects.get(user=request.user)
            except Public.DoesNotExist:
                # If the profile does not exist, redirect to the profile page
                return redirect('profile')
    return render(request, 'home.html')

@login_required(login_url='login')
def police_dashboard(request):
    # Your police dashboard view logic here
    return render(request, 'police_dashboard.html')

#@login_required(login_url='login')
#def profile(request):
    profile, created = Public.objects.get_or_create(user=request.user)  # Efficient profile lookup
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        location = request.POST.get('location')

        # Update the profile details (assuming Public model has appropriate fields)
        profile.name = name
        profile.age = age
        profile.gender = gender
        profile.phone = phone
        profile.email = email
        profile.location = location
        profile.save()

        # Optionally, you can add additional validation or error handling here,
        # such as checking for empty or invalid data.

        return redirect('home')  # Redirect to home page after saving profile

    context = {'profile': profile}
    return render(request, 'profile.html', context)


from django.shortcuts import redirect
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    context={}
    return render(request,'home.html',context)

def profile(request):
    context={}
    return render(request,'profile.html',context)

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

