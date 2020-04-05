from django.shortcuts import render
from .forms import TeacherSignUpForm
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'user/signup.html')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'teacher/teacher_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)
 