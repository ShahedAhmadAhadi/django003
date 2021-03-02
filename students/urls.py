from django.urls import path
from .views import initial, add_student

app_name = 'students'

urlpatterns = [
    path('', initial, name="initial"),
    path('add/', add_student, name="add_student"),
]