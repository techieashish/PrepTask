from django.test import TestCase
from .models import University


class UniversityTestCase(TestCase):
    def setUp(self):
        University.objects.create(name="MIT", courses="Engineering")
        University.objects.create(name="IIT", courses="Engineering")

    def test_university(self):
        e2 = University.objects.get(name="IIT")
        self.assertEqual(e2.courses, "Engineering")