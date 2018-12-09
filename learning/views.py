from django.shortcuts import render, redirect, get_object_or_404
from .models import University, Student, Classes
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from .forms import UniversityForm, StudentForm, ClassesForm, Registration, Login
from .serializers import StudentSerializers, UniversitySerializer, ClassesSerializers
from django.contrib.auth import login, logout, authenticate


def index(request):
    return render(request=request, template_name="hello.html")


def UserRegistration(request):
    form = Registration(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("learn:index")
    return render(request, "hello.html", {"form": form})

def user_login(request):
    form = Login(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user.is_active and user is not None:
            login(request, user)
            return redirect("learn:index")
    return render(request, "message.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("learn:index")


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializers


class UniveristyViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


# Used to learn different ORM techniques

def query_set_practice(request):
    # To do OR or AND operations on query sets we use | or & operators repectively.
    # Below is the example of the same.
    #queryset = Student.objects.filter(name__startswith="A") & Student.objects.filter(name__endswith="a")
    #queryset = Student.objects.filter(name__startswith="A").values("name", "roll_number") & Student.objects.filter(name__endswith="a").values("name", "roll_number")

    # Performing SQL joins, In django we use select_related for SQL level joins on model which use one-to-may relationship
    # and prefetch_related which joins on Python level mostly used with many-to-many relationship

    # queryset = Student.objects.select_related("university").all()
    # for data in queryset:
        # print(data.university, data.university.id, data.university.courses)

    # To find second largest value, use order_by("column_name")[index] initialized at 0
    # Example:-

    #queryset = University.objects.order_by("-id")[1]

    # Find rows which have duplicate field values

    queryset = Student.objects.values("name").annotate(name_count=Count("name")).filter(name_count__get=1)

    return render(request=request, template_name="message.html", context={"message": queryset})

