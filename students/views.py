from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from students.forms import StudentForm
from students.models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.


def search(request, name):
    a = Student.objects.all()
    count = 1
    # print(name)
    for i in a:
        for y in i.s_name:
            if y == name:
                count += 1
                
                print(i.s_name)
                print()
            return JsonResponse({"hi":i.s_name})



def initial(request):
    stu_lst = Student.objects.all()
    context = {
        'stu_lst': stu_lst
    }

    return render(request, 'students/index.html', context)

def detail(request, roll_no):
    lst = Student.objects.get(s_roll = roll_no)
    context = {
        'lst': lst
    }
    return render(request, 'students/detail.html', context)

@login_required
def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('../../home/')
    
    return render(request, 'students/student-form.html', {'form': form})

@login_required
def update_student(request, roll_no=None):
    if roll_no:
        student = Student.objects.get(s_roll = roll_no)
        form = StudentForm(data=request.POST or None, files=request.FILES or None, instance=student)

        if form.is_valid():
            form.save()
            return redirect('../../home/')
        

        return render(request, 'students/update.html', {'form': form})

@login_required
def delete_student(request, roll_no):
    student = Student.objects.get(s_roll = roll_no)

    if request.method == "POST":
        student.delete()
        return redirect('../../home')
    
    return render(request, 'students/delete.html', {'student': student})


