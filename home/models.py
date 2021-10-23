# Bismillah Hir Rehman Nir Rahim

from os import name
from django.contrib import auth
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

# class Contact(models.Model):
#     Name=models.CharField(max_length=30)
#     Email=models.CharField(max_length=50)
#     Phone=models.CharField(max_length=10)
#     Problem=models.TextField(max_length=200)


#     def __str__(self):
#      return self.Problem

class Contactus(models.Model):
    mainuse=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=10)
    Problem=models.TextField(max_length=200)


    def __str__(self):
     return self.Problem






class Users(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)

    def __str__(self):
        return self.email



# class UserEarning(models.Model):
#     users=models.ForeignKey(User , on_delete=models.CASCADE , default="",editable=False)
#     video=models.CharField(max_length=40)
#     earning=models.IntegerField()
#     livevids=models.IntegerField()

# class Userearns(models.Model):
#     user=models.ForeignKey(User , on_delete=models.CASCADE)
#     video=models.CharField(max_length=40)
#     earning=models.IntegerField()
#     livevids=models.IntegerField()

class Userearns12(models.Model):
   
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    video=models.CharField(max_length=40)
    earning=models.IntegerField()
    livevids=models.IntegerField()


# class add_bank_details(models.Model):
#     user=models.ForeignKey(User , on_delete=models.CASCADE)
#     acc_number=models.CharField(max_length=20)
#     acc_name=models.CharField(max_length=30)    
#     swift_code=models.CharField(max_length=20)


class add_bank_details_user(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    acc_number=models.CharField(max_length=20)
    acc_name=models.CharField(max_length=30)    
    swift_code=models.CharField(max_length=20)
    profile_name=models.CharField(max_length=100,default=1)
    profile_url=models.CharField(max_length=400,default=1)
    


    
    def __str__(self):
     return self.user.email


# class userwhosubs(models.Model):
#     usersubs=models.ForeignKey(User,on_delete=models.CASCADE)  
















