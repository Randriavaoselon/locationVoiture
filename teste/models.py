from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from users.models import Profile

# Create your models here.
class Search(models.Model):
    adresse = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adresse
    
class department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    departmentname = models.CharField(max_length=100)

    def __str__(self):
        return self.departmentname
    
    
class employee(models.Model):
    deptid = models.ForeignKey(department,on_delete=CASCADE)
    userProf = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="userprof", null=True)
    empname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=500, null=True)
    contactno = models.CharField(max_length=20)   

    def __str__(self):
        return self.empname


class Car(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Model(models.Model):
    name = models.CharField(max_length=100)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car}-{self.name}"
    

class Image(models.Model):
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption
    
    
             
     

   
