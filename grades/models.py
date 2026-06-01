from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    obtained_marks = models.IntegerField()
    total_marks = models.IntegerField()

    def percentage(self):
        return (self.obtained_marks / self.total_marks) * 100

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A"
        return "F"
    