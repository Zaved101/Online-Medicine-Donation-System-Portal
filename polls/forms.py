from django import forms
from .models import Patient
from .models import Medicine
from .models import Provided_Medicine
from .models import User

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_ID', 'Patient_Name','Patient_Address','Patient_Phone_Number', 'Patient_Age', 'Patient_Diseases']


class PatientForm2(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_Rx','Medicine_morning','Medicine_noon','Medicine_night','Per_day','Total_medicine']

class PatientForm3(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_Rx']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['Medicine_Name', 'Medicine_Type','Medicine_Mg','Medicine_Expiriy_Date','Medicine_Quantity']


class Provided_MedicineForm(forms.ModelForm):
    class Meta:
        model =Provided_Medicine
        fields = ['Patient_ID', 'Patient_Name','Patient_Address','Provided_Medicine']


# class UserUpdateForm(forms.ModelForm):
#     email=forms.EmailField()
#     class Meta:
#         model= User
#         fields= [ 'doctor_phone_number','doctor_address','image']