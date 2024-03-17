from django.db import models
from django.contrib import admin

class Public(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Display the user's name in the admin interface

class PublicAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'email', 'phone', 'location')


# Model to represent Global application configuration
class GlobalConfig(models.Model):
    name = models.CharField(max_length=100)
    # status = Enabled, Disabled
    status = models.CharField(max_length=10)
    int_value = models.IntegerField()
    string_value = models.CharField(max_length=100)
    float_value = models.FloatField()
    date_value = models.DateTimeField()
    description = models.TextField()

class GlobalConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'int_value', 'string_value', 'float_value', 'date_value', 'description')

class PoliceStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    officers_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name  # Display the police station name

class PoliceStationAdmin(admin.ModelAdmin):
    list_display=('name','location','capacity','officers_count')
