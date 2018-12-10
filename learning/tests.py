from django.test import TestCase
from .models import University, Student


class UniversityTestCase(TestCase):
    def setUp(self):
        University.objects.create(name="MIT", courses="Engineering")
        University.objects.create(name="IIT", courses="Engineering")

    def test_university(self):
        e2 = University.objects.get(name="IIT")
        self.assertEqual(e2.courses, "Engineering")
        e3 = University.objects.get(courses="Engineering")
        self.assertEqual(e3.courses, "MIT")
        

class StudentTestCase(TestCase):

    def setUp(self):
        mit = University.objects.get(name="MIT")
        Student.objects.create(name="Mark", roll_number=900, gender="Male", university=mit)

    def test_student(self):
        mark = Student.objects.get(name="Mark")
        self.assertEqual(mark.university, "MIT")
