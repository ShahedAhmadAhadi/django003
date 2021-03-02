from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.forms import StudentForm
from students.models import Student

# Create your views here.

def initial(request):
    stu_lst = Student.objects.all()
    context = {
        'stu_lst': stu_lst
    }

    return render(request, 'students/index.html', context)


def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('students/index.html')
    
    return render(request, 'students/student-form.html', {'form': form})

