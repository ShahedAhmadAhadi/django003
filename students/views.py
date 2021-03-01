from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.views.generic.edit import CreateView

# Create your views here.

def initial(request):
    return render(request, 'students/index.html')


class AddStudent(CreateView):
    model = Student
    fields = ['s_roll' ,'s_name','s_father_name', 's_birth', 's_phone', 's_email', 's_image']
    template_name = 'students/student-form.html'

