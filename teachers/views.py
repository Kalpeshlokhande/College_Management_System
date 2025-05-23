from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import ClassRoom, Subject
from .models import Assignment, Announcement

@login_required
def teacher_dashboard(request):
    teacher = request.user
    classes = teacher.teaching_classes.all()
    subjects = Subject.objects.filter(classroom__in=classes).distinct()
    assignments = Assignment.objects.filter(teacher=teacher)
    announcements = Announcement.objects.filter(teacher=teacher)
    return render(request, 'dashboard/teacher_dashboard.html', {
        'classes': classes,
        'subjects': subjects,
        'assignments': assignments,
        'announcements': announcements,
    })

@login_required
def teacher_assignments(request):
    teacher = request.user
    classes = teacher.teaching_classes.all()
    if request.method == 'POST':
        classroom_id = request.POST['classroom']
        title = request.POST['title']
        file = request.FILES['file']
        Assignment.objects.create(
            classroom_id=classroom_id,
            teacher=teacher,
            title=title,
            file=file
        )
        return redirect('teacher_assignments')
    assignments = Assignment.objects.filter(teacher=teacher)
    return render(request, 'dashboard/teacher_assignments.html', {'classes': classes, 'assignments': assignments})

@login_required
def teacher_announcements(request):
    teacher = request.user
    classes = teacher.teaching_classes.all()
    if request.method == 'POST':
        classroom_id = request.POST['classroom']
        content = request.POST['content']
        Announcement.objects.create(
            classroom_id=classroom_id,
            teacher=teacher,
            content=content
        )
        return redirect('teacher_announcements')
    announcements = Announcement.objects.filter(teacher=teacher)
    return render(request, 'dashboard/teacher_announcements.html', {'classes': classes, 'announcements': announcements})