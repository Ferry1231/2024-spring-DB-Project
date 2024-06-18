# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course, Grade
from .forms import CourseSelectionForm

def course_selection(request):
    if request.method == 'POST':
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-selection-success')
    else:
        form = CourseSelectionForm()
    return render(request, 'course_selection.htm', {'form': form})

def drop_course(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('course-selection-success')
    return render(request, 'drop_course.htm', {'grade': grade})

def course_selection_success(request):
    return render(request, 'course_selection_success.htm')

