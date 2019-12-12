from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import User

class Patient(models.Model):
    medicine_choice = [
        ('Renava','Renava'),
        ('napa','napa'),
        ('opton','opton'),
        ('ctz','ctz'),
    ]

    Patient_ID = models.AutoField(primary_key=True)
    Patient_Name=models.CharField(max_length=200)
    Patient_Address=models.CharField(max_length=200)
    Patient_Phone_Number=models.CharField(max_length=200)
    Patient_Age = models.CharField(max_length=200)
    Patient_Diseases=models.TextField(max_length=200)
    Patient_Rx = models.CharField(choices=medicine_choice,max_length=40,null=True,blank=True)
    Medicine_morning =models.BooleanField(default=False)
    Medicine_noon = models.BooleanField(default=False)
    Medicine_night = models.BooleanField(default=False)
    Per_day=models.CharField(max_length=200)
    Total_medicine = models.CharField(max_length=200)




    #Date = models.DateField('date published')


    def __str__(self):
        return self.Patient_Name


# class User(AbstractUser):
#     doctor_phone_number=models.CharField(max_length=20)
#     doctor_address=models.CharField(max_length=20)
#     image=models.ImageField(default='default.jpg',upload_to='profile_Pic')

class Medicine(models.Model):
    Medicine_Name=models.CharField(max_length=200)
    Medicine_Type=models.CharField(max_length=200)
    Medicine_Mg = models.IntegerField()
    Medicine_Expiriy_Date = models.CharField(max_length=200)
    Medicine_Quantity = models.IntegerField()

    def __str__(self):
        return self.Medicine_Name

class Provided_Medicine(models.Model):
    Patient_ID = models.CharField(max_length=200)
    Patient_Name=models.CharField(max_length=200)
    Patient_Address = models.CharField(max_length=200)
    Provided_Medicine=models.TextField(max_length=200)

    def __str__(self):
        return self.Patient_ID
