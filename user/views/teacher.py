from django.shortcuts import render, redirect
from user.forms import TeacherSignUpForm
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from user.models import User
# Create your views here.

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'teacher/teacher_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('index')