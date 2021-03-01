from django.urls import path
from .views import initial

app_name = 'students'

urlpatterns = [
    path('', initial, name="initial")
]