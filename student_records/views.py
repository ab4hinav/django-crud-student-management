from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# READ - Display all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_records/student_list.html', {
        'students': students
    })


# CREATE - Add a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'student_records/student_form.html', {
        'form': form
    })


# UPDATE - Edit an existing student
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_records/student_form.html', {
        'form': form
    })


# DELETE - Delete a student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

    return redirect('student_list')