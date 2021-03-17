from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from students.forms import StudentForm
from students.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core import serializers


# Create your views here.


# def not_user():
#     if not User.is_authenticated:
#         redirect('../../login')

# @login_required(login_url='/login/')
def search(request):
    # print(request.GET)
    count = 0
    res = {}
    search_results = Student.objects.filter(s_name__icontains = request.GET['text'])
    pages = Paginator(search_results, 4)
    # print(pages)
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = pages.get_page(page_number)
    # print(page_obj)
    for i in page_obj:
        print(i)
    # print(page_obj.__dict__.update('a', page_obj))
    res = serializers.serialize('json', page_obj)
    # print(res)

    # for i in search_results:
    #     count += 1
    #     res.update({f"res{count}": {'id':f"{i.s_name[1:2]}{i.s_father_name[1:2]}{int(i.s_roll * 1234)}", 'name': i.s_name, 'f/name': i.s_father_name, 'phone': i.s_phone, 'roll_no': i.s_roll}})
    # 
    if len(res) < 1:
        return JsonResponse({'res': 'none'})
    else:
        return JsonResponse({'res': res})



# @login_required(login_url='/login/')
# def initial(request):
#     # stu_lst = Student.objects.all()
#     # context = {
#     #     'stu_lst': stu_lst
#     # }

#     # return render(request, 'students/index.html', context)

class Index(ListView):
    paginate_by = 4
    model = Student

@login_required(login_url='/login/')
def detail(request, roll_no):
    lst = Student.objects.get(s_roll = roll_no)
    context = {
        'lst': lst
    }
    return render(request, 'students/detail.html', context)

@login_required(login_url='/login/')
def add_student(request):
    form = StudentForm(request.POST, request.FILES)

    # print(request.POST, request.FILES,  form.is_valid(), form)

    if form.is_valid():
        print(form, 'a')
        form.save()
        return redirect('/home/')
    
    
    return render(request, 'students/student-form.html', {'form': form})

@login_required(login_url='/login/')
def update_student(request, roll_no=None):
    if roll_no:
        student = Student.objects.get(s_roll = roll_no)
        form = StudentForm(data=request.POST or None, files=request.FILES or None, instance=student)

        if form.is_valid():
            form.save()
            return redirect('/home/')
        

        return render(request, 'students/update.html', {'form': form})

@login_required(login_url='/login/')
def delete_student(request, roll_no):
    lst = Student.objects.get(s_roll = roll_no)

    if request.method == "POST":
        lst.delete()
        return redirect('/home/')
    
    return render(request, 'students/delete.html', {'lst': lst})


