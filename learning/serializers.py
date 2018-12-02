from rest_framework import serializers
from .models import University, Student, Classes


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "_all_"


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class ClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"

