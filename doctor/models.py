from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# docotr gives rx to patients
class Patient_Rx(models.Model):
    Patient_ID = models.IntegerField()
    Patient_Name=models.CharField(max_length=200)
    Patient_Age=models.CharField(max_length=200)
    Patient_Precribed=models.TextField(max_length=200)

    def __str__(self):
        return self.Patient_Name

# doctor profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor_name=models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)