from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path,include
from user.views import views
from user.views import teacher

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name="login"),

    path('signup/',include([
        path('', views.signup, name='signup'),
        path('teacher_signup/', teacher.TeacherSignUpView.as_view(), name='teacher_signup'),

    ]))
]
