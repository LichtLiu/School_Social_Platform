from django.shortcuts import render, redirect
from user.forms import TeacherSignUpForm
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'user/signup.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
