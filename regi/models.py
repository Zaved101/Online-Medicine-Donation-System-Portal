from django.db import models

class give_medi(models.Model):
    Medicine_Name = models.CharField(max_length=200)
    Medicine_Type = models.CharField(max_length=200)
    Medicine_Mg = models.IntegerField()
    Medicine_Expiriy_Date = models.CharField(max_length=200)
    Medicine_Quantity = models.IntegerField()

    def __str__(self):
        return self.Medicine_Name


class regi(models.Model):
    Company_Name = models.CharField(max_length=200)
    # Email = models.CharField(max_length=200)