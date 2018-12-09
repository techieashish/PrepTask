from django import forms
from .models import University, Student, Classes
from django.contrib.auth.admin import User


class Login(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class Registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:

        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

class UniversityForm(forms.ModelForm):

    class Meta:
        model = University
        fields = "__all__"


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"


class ClassesForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"

