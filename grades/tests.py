from django.test import TestCase
from .models import Student

class GradeTest(TestCase):

    def test_grade_a(self):
        student = Student(
            name="Shivam",
            obtained_marks=450,
            total_marks=500
        )

        self.assertEqual(student.grade(), "A")