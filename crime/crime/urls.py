"""
URL configuration for crime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crimeapp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),  # Use user_login view for login
    path('police_dashboard/', views.police_dashboard, name='police_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('emergency/', views.emergency, name='emergency'),
    path('complient/', views.complient, name='complient'),
    path('result/', views.result, name='result'),
    path('public_emergence/', views.public_emergence, name='public_emergence'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

