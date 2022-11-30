from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=50 ,default="")
    father_name = models.CharField(max_length=50 ,default="")
    gender = models.CharField(max_length=50 ,default="")
    Class = models.CharField(max_length=50 ,default="")
    section = models.CharField(max_length=50 ,default="") 
    roll_no = models.CharField(max_length=50 ,default="")
    native_country = models.CharField(max_length=50,default="")
    native_language = models.CharField(max_length=50,default="")
    language_to_learn = models.CharField(max_length=50,default="")
    photo = models.FileField(upload_to="myimage",default="")
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class madarsa(models.Model):
    name = models.CharField(max_length=50 ,default="")
    father_name = models.CharField(max_length=50 ,default="")
    gender = models.CharField(max_length=50 ,default="")
    Class = models.CharField(max_length=50 ,default="")
    section = models.CharField(max_length=50 ,default="") 
    roll_no = models.CharField(max_length=50 ,default="")
    native_country = models.CharField(max_length=50,default="")
    native_language = models.CharField(max_length=50,default="")
    language_to_learn = models.CharField(max_length=50,default="")
    photo = models.ImageField(upload_to="madarsa",default="")
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name



class contact(models.Model):
    name = models.CharField(max_length=50 ,default="")
    email = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name


    
# name                                                                  
# father_name                                                                  
# gender                                                                  
# Class                                                                  
# section                                                                  
# roll_no                                                                  
# photo                                                                  
# date                                                                  
# native_country                                                                  
# native_language                                                                  
# language_to_learn                                                                  