from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def initial(request):
    return render(request, 'students/index.html')
