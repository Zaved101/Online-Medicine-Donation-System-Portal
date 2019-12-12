from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,get_object_or_404,redirect

from django.views.generic.edit import CreateView
from polls.forms import PatientForm,PatientForm3,PatientForm2
from polls.models import Patient

from polls.forms import MedicineForm
from polls.models import Medicine

from polls.forms import Provided_MedicineForm
from polls.models import Provided_Medicine

from django.http import HttpResponse
from doctor.models import Patient_Rx
from regi.models import give_medi

# login_code
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'polls/web.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'doctor/login.html')

# homepage
def index(request):
    return render(request, 'polls/web.html')

#patientinfo_store
def store(request):
    if request.method == "POST":
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('StorePatientInformation')
    else:
        form = PatientForm()
    return render(request,'polls/patient.html',{'form':form})

# give doctor rx
def showrx(request):
    rx = Patient_Rx.objects.all()
    return render(request,'polls/adminshow.html',{'rx':rx})

#store_medicine
def store_Medi(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('store')
            except:
                pass
    else:
        form = MedicineForm()
    return render(request,'polls/storemedicine.html',{'form':form})

# gives a medicine to patient
def provide_Medi(request):
    if request.method == "POST":
        form = Provided_MedicineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('provide')
            except:
                pass
    else:
        form = Provided_MedicineForm()
    return render(request,'polls/provide.html',{'form':form})

# admin can view patient info
def viewstore(request):
     stored = Patient.objects.all()
     data = {'patients': stored}
     return render(request, 'polls/View.html', data)


# who gives medicine
def givemediview(request):
    medi = give_medi.objects.all()
    return render(request,'polls/giveview.html',{'medi':medi})


# patient info delete
def deleteStore(request, pk, template_name='polls/Store_Confirm_Delete.html'):
    deleting = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        deleting.delete()
        return redirect('StorePatientInformationView')
    return render(request, template_name, {'object': deleting})


# patinet info edit
def updateStore(request,pk):
    training = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=training)
    if form.is_valid():
        form.save()
        return redirect("StorePatientInformationView")
    return render(request, 'polls/patient.html', {'form': form})

# patient give medicine a doctor
def givemedicine(request,pk):
    training = get_object_or_404(Patient, pk=pk)
    u_form = PatientForm(request.POST or None, instance=training)
    q_form = PatientForm3(request.POST, instance=training)
    if u_form.is_valid() and q_form.is_valid():
        u_form.save()
        q_form.save()
        return redirect('StorePatientInformationView')
    context = {
        'u_form':u_form,
        'q_form':q_form
    }
    return render(request, 'polls/mediForm.html', context)


# log out
def user_logout(request):
    logout(request)
    return render(request,'polls/login.html')