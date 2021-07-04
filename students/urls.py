from django.urls import path
from .views import initail

# app_name = 'students'

urlpatterns=[
    path('', initail, name='main'),

]