from django.urls import path
from .views import add_student

app_name = 'students'

urlpatterns = [
    # path('', initial, name="initial"),
    # path('add/', add_student, name="add"),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
