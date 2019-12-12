from django import forms
from .models import Patient_Rx
from .models import Profile



class Patient_RxForm(forms.ModelForm):
    class Meta:
        model = Patient_Rx
        fields = ['Patient_ID', 'Patient_Name', 'Patient_Age', 'Patient_Precribed']

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image','doctor_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','doctor_name']