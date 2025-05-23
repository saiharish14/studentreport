from django.db import models

class Student(models.Model):
    roll_number = models.IntegerField(unique=True)  # Or remove 'unique=True' if you don’t want it
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    student_class = models.CharField(max_length=20)
    marks = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"
