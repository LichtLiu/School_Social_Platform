from django import forms
from django.forms.utils import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Subject

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user
