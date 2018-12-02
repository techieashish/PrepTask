from django.shortcuts import render
from .models import University, Student, Classes
from django.db.models import Count
from .serializers import StudentSerializers, UniversitySerializer
from rest_framework import viewsets


def index(request):
    return render(request=request, template_name="hello.html")


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers()


class UniversityView(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer()

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

