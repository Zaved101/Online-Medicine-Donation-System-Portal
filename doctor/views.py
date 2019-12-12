from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from doctor.forms import Patient_RxForm
from doctor.models import Patient_Rx
from polls.forms import PatientForm,PatientForm2
# Create your views here.
from polls.models import Patient
from agent.models import Patient_Information

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from regi.forms import UserRegisterForm,UserUpdateForm
from .models import Profile
from doctor.forms import ProfileUpdateForm


def updateStore(request,pk):
    training = get_object_or_404(Patient, pk=pk)
    u_form = PatientForm(request.POST or None, instance=training)
    p_form = PatientForm2(request.POST, instance=training)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        return redirect('show')
    # else:
        # u_form = PatientForm()
        # p_form= PatientForm2()
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'doctor/RXFrom.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'doctor/doctor.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'doctor/login.html')

def user_logout(request):
    logout(request)
    return render(request,'doctor/login.html')

def show(request):
    patients = Patient.objects.all()
    return render(request,'doctor/doctorshow.html',{'patients':patients})


def give_pre(request):
    if request.method == "POST":
        form = Patient_RxForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('give')
            except:
                pass
    else:
        form = Patient_RxForm()
    return render(request,'doctor/give.html',{'form':form})

def profile(request):
    return render(request, 'doctor/Profile.html')

def upprofile(request):
    if request.method == 'POST':
        a_form = UserUpdateForm(request.POST, instance=request.user)
        b_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if a_form.is_valid() and b_form.is_valid():
            a_form.save()
            b_form.save()
            # messages.success(request, f'Your account has been updated!')
            return redirect('profileview')

    else:
        a_form = UserUpdateForm(instance=request.user)
        b_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'a_form': a_form,
        'b_form': b_form
    }

    return render(request, 'doctor/upprofile.html', context)



