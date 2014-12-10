from django.shortcuts import render, get_object_or_404

# Create your views here.
from students.models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',
                  {'students': students})


def student_info(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html',
                  {'student': student})
