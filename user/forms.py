from django import forms
from django.forms.utils import ValidationError
from django.db import transaction
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


class StudentSignUpForm(UserCreationForm):
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.Select,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.subject.add(*self.cleaned_data.get('subject'))
        return user