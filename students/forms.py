from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['s_name','s_father_name', 's_birth', 's_phone', 's_email', 's_image']
        widgets = {
            's_name': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none'}),
            's_father_name': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none'}),
            's_birth': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none', 'type': 'date'}),
            's_phone': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none'}),
            's_email': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none', 'type': 'email'}),
            's_image': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none', 'type': 'file'}),
        }
