from django.db import models


class Patient_Information(models.Model):
    Patient_ID = models.AutoField(default=1,primary_key=True)
    Patient_Name=models.CharField(max_length=200)
    Patient_Address=models.CharField(max_length=200)
    Patient_Phone_Number=models.CharField(max_length=200)
    Patient_Age = models.CharField(max_length=200)
    Patient_Diseases=models.TextField(max_length=200)

    def __str__(self):
        return self.Patient_Name

class give_medi(models.Model):
    Medicine_Name = models.CharField(max_length=200)
    Medicine_Type = models.CharField(max_length=200)
    Medicine_Mg = models.IntegerField()
    Medicine_Expiriy_Date = models.CharField(max_length=200)
    Medicine_Quantity = models.IntegerField()

    def __str__(self):
        return self.Medicine_Name

