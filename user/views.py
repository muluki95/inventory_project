from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def register (request):
    if request.method == 'POST':
       form = CreateUserForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('user-login')
    else:   
       form = CreateUserForm()
    context = {
        'form':form
    }
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    
    return render(request, 'user/profile_update.html')