"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authentication_views
from students.views import add_student, update_student, delete_student, detail,search, Index
from users.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Index.as_view(template_name="students/index.html"), name="home"),
    path('', include('students.urls')),
    path('home/<int:roll_no>/', detail, name="detail"),
    path('add/', add_student, name='add'),
    path('delete/<int:roll_no>/', delete_student, name='delete'),
    path('update/<int:roll_no>/', update_student, name='update'),
    path('signup/', include('users.urls'), name="signup"),
    path('login/', authentication_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    # path('logout/', authentication_views.LogoutView.as_view(template_name="users/login.html"), name='logout'),
    path('logout/', logout, name="logout"),
    path("search/", search, name="search")
]
