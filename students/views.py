from django.shortcuts import render
from students.models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def student_item(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/item.html', {'student': student})
