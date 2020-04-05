from django.contrib import admin
from django.urls import path,include
from user import views

urlpatterns = [
    
    path('signup/',include([
        path('', views.signup, name='signup'),
        path('teacher_signup/', views.TeacherSignUpView.as_view(), name='teacher_signup'),

    ]))
]
