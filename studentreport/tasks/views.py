from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

def student_list(request):
    students = Student.objects.all()
    return render(request, 'tasks/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'tasks/student_form.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'tasks/student_form.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'tasks/student_confirm_delete.html', {'student': student})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Authenticated successfully!'}
        return Response(content)
