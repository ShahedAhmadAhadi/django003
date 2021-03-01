from django.urls import path
from .views import initial, AddStudent

app_name = 'students'

urlpatterns = [
    path('', initial, name="initial"),
    path('', AddStudent.as_view(), name="add_student"),
]