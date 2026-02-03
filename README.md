# Ex01 Django ORM Web Application
## Date: 31.01.2026

## AIM
To develop a Django Application to store and retrieve data from Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class swiggyDB(models.Model):
    Mobile_no=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    price=models.FloatField()
    Email=models.EmailField()
    Date=models.DateField()
    Bill_no=models.IntegerField()
    Items_no=models.IntegerField()
class swiggyDBAdmin(admin.ModelAdmin):
	list_display=['Mobile_no','Name','price','Email','Date','Bill_no','Items_no'];

admin.py
from django.contrib import admin
from .models import swiggyDB,swiggyDBAdmin
admin.site.register(swiggyDB,swiggyDBAdmin)
```


## OUTPUT
![alt text](<Screenshot (17).png>)


## RESULT
Thus the program for creating online food delivery website database using ORM hass been executed successfully
