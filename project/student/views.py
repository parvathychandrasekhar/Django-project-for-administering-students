from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect,get_object_or_404
from .forms import StudentForm
from .models import Student



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            physics_marks = form.cleaned_data['physics_marks']
            chemistry_marks = form.cleaned_data['chemistry_marks']
            maths_marks = form.cleaned_data['maths_marks']
            computer_science_marks = form.cleaned_data['computer_science_marks']


            if physics_marks > 100:
                form.add_error('physics_marks', 'Physics marks cannot be greater than 100.')
            if chemistry_marks > 100:
                form.add_error('chemistry_marks', 'Chemistry marks cannot be greater than 100.')
            if maths_marks > 100:
                form.add_error('maths_marks', 'Maths marks cannot be greater than 100.')
            if computer_science_marks > 100:
                form.add_error('computer_science_marks', 'Computer Science marks cannot be greater than 100.')
            name = form.cleaned_data['name']
            if Student.objects.filter(name=name).exists():
                form.add_error('name', 'A student with this name already exists.')
                context = {'form': form}
                return render(request, 'add_student.html', context)
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
def delete_confirm(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect('student_list')
    else:
        students = Student.objects.all()
        context = {'students': students}
        return render(request, 'delete.html', context)

