from django.shortcuts import render, redirect
from regi.forms import give_mediForm
from regi.models import give_medi
from .forms import UserRegisterForm

def give_medi(request):
    if request.method == "POST":
        form = give_mediForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('donner_medi')
            except:
                pass
    else:
        form = give_mediForm()
    return render(request,'regi/donner_medi.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('donner_medi')
    else:
        form = UserRegisterForm()
    return render(request, 'regi/registration.html', {'form': form})
