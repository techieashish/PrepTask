from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)
    courses = models.CharField(max_length=500)

    def __str__(self): return self.name


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    university = models.ForeignKey(University, primary_key=True, blank=True)

    def __str__(self): return self.name


class Classes(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, blank=True, related_name="students")

    def __str__(self): return self.name
