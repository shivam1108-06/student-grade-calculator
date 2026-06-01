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

    def test_grade_b(self):
        student = Student(
        name="Shivam",
        obtained_marks=425,
        total_marks=500
    )
        self.assertEqual(student.grade(), "B")

    def test_grade_c(self):
        student = Student(
            name="Shivam",
            obtained_marks=375,
            total_marks=500
        )
        self.assertEqual(student.grade(), "C")

    def test_grade_d(self):
        student = Student(
            name="Shivam",
            obtained_marks=325,
            total_marks=500
        )
        self.assertEqual(student.grade(), "D")