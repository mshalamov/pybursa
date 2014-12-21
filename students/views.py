from django.shortcuts import render, redirect, get_object_or_404

from students.models import Student, StudentForm, StudentModelForm


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',
                  {'students': students})


def student_info(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html',
                  {'student': student})


def student_edit(request, student_id):
    title = "Edit Student"
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.package = form.cleaned_data['package']
            student.save()
            return redirect('student_edit', student_id)
    else:
        form = StudentForm(initial={'first_name': student.first_name,
                                    'last_name': student.last_name,
                                    'package': student.package})
    return render(request,
                  'students/student_edit.html',
                  {'form': form, 'title': title})


def student_add(request):
    title = "Add Student"
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_edit', student.id)
    else:
        form = StudentModelForm()
    return render(request,
                  'students/student_edit.html',
                  {'form': form, 'title': title})
