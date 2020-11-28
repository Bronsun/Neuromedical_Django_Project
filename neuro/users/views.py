from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    title = "Rejestracja | Neuromedical App"
    if request.method == 'POST': 
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone!')
            return redirect('main-home')
    else:
        form = UserRegisterForm()
        
    return render(request,'register/register.html',{'form': form,'title':title})
