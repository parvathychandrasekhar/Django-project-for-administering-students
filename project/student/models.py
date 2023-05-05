from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    physics_marks = models.PositiveIntegerField()
    chemistry_marks = models.PositiveIntegerField()
    maths_marks = models.PositiveIntegerField()
    computer_science_marks = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)



    def __str__(self):
        return self.name