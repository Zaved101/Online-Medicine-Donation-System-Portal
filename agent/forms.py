from django import forms
from .models import Patient_Information
from .models import give_medi


class Patient_InformationForm(forms.ModelForm):
    class Meta:
        model = Patient_Information
        fields  = ['Patient_ID', 'Patient_Name','Patient_Address','Patient_Phone_Number', 'Patient_Age', 'Patient_Diseases']

class give_mediForm(forms.ModelForm):
    class Meta:
        model = give_medi
        fields  = ['Medicine_Name', 'Medicine_Type','Medicine_Mg','Medicine_Expiriy_Date','Medicine_Quantity']

