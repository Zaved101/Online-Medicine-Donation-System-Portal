from django.shortcuts import render,redirect
from agent.forms import Patient_InformationForm
from agent.models import Patient_Information

from agent.forms import give_mediForm
from agent.models import give_medi
from polls.models import Patient
from polls.forms import PatientForm


def index(request):
    return render(request, 'agent/web.html')

def storeAgent(request):
    if request.method == "POST":
        form = PatientForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('patientAgent')
    else:
        form = PatientForm()
    return render(request,'agent/patient.html',{'form':form})

def medistore(request):
    if request.method == "POST":
        form = give_mediForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('')
            except:
                pass
    else:
        form = give_mediForm()
    return render(request,'agent/storemedicine.html',{'form':form})
