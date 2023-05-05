from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            total_marks = student.physics_marks + student.chemistry_marks + student.maths_marks + student.computer_science_marks
            student.percentage = round((total_marks / 400)*100, 2)
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
