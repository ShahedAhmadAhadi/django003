from django.shortcuts import render
from .forms import Register

# Create your views here.

def login(request):
    
    return render(request, 'users/index.html')

def signup(request):
    form = Register
    return render (request, 'users/index.html', {'form':form})
