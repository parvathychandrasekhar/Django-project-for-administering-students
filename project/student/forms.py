from django import forms
from .models import Student
from django.forms.widgets import DateInput

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'physics_marks', 'chemistry_marks', 'maths_marks', 'computer_science_marks']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }

