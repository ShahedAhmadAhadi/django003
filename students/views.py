from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from students.forms import StudentForm
from students.models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.


def search(request, name):
    count = 0
    res = {}
    print(res)
    a = Student.objects.filter(s_name__contains = name)
    for i in a:
        count += 1
        res.update({f"res{count}": {'id':f"{i.s_name[1:2]}{i.s_father_name[1:2]}{int(i.s_roll * 1234)}", 'name': i.s_name, 'f/name': i.s_father_name, 'phone': i.s_phone, 'roll_no': i.s_roll}})
    return JsonResponse(res)

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
    lst = Student.objects.get(s_roll = roll_no)

    if request.method == "POST":
        lst.delete()
        return redirect('../../home')
    
    return render(request, 'students/delete.html', {'lst': lst})


