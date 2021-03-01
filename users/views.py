from django.shortcuts import render, redirect
from .forms import Register

# Create your views here.

def login(request):

    
    return render(request, 'users/login.html')

def signup(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Register()
    return render (request, 'users/index.html', {'form':form})
