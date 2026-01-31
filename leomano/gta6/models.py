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


