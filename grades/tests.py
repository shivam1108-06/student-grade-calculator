from django.test import TestCase
from .models import Student 

# Create your tests here.

class GradeTestCase(TestCase):
    
    def test_grade_a(self):
        student = Student(name='Shivam', obtained_marks=450, total_marks=500)
        self.assertEqual(student.grade(), 'A')