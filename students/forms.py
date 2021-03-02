from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['s_name','s_father_name', 's_birth', 's_phone', 's_email', 's_image']
