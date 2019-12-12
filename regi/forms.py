from django import forms
from .models import give_medi
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class give_mediForm(forms.ModelForm):
    class Meta:
        model = give_medi
        fields = ['Medicine_Name', 'Medicine_Type', 'Medicine_Mg', 'Medicine_Expiriy_Date', 'Medicine_Quantity']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',]