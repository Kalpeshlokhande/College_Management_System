from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from teachers.models import Assignment, Announcement

@login_required
def student_dashboard(request):
    student = request.user
    classrooms = student.classrooms.all()
    assignments = Assignment.objects.filter(classroom__in=classrooms)
    announcements = Announcement.objects.filter(classroom__in=classrooms)
    return render(request, 'dashboard/student_dashboard.html', {
        'classrooms': classrooms,
        'assignments': assignments,
        'announcements': announcements,
    })

@login_required
def view_assignments(request):
    student = request.user
    assignments = Assignment.objects.filter(classroom__in=student.classrooms.all())
    return render(request, 'dashboard/view_assignments.html', {'assignments': assignments})