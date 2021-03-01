from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

def validate_age(value):
        today = date.today()
        if today.year - value.year < 5:
            raise Exception('Sorry, you are not at age to enter the school')

class Student(models.Model):

    s_roll = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=30, null=False)
    s_father_name = models.CharField(max_length=30, null=False)
    s_birth = models.DateField(validators=[validate_age])
    s_phone = models.IntegerField(unique=True)
    s_email = models.EmailField(unique=True)
    user_add = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


