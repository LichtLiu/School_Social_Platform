from django.shortcuts import render, redirect
from user.forms import TeacherSignUpForm
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'user/signup.html')

