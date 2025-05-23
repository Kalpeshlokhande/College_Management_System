from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ClassSchedule, DAYS
from core.models import ClassRoom, Subject
from django.contrib.auth.models import User

@login_required
def manage_schedule(request):
    classes = ClassRoom.objects.all()
    subjects = Subject.objects.all()
    teachers = User.objects.filter(profile__role='teacher')
    schedules = ClassSchedule.objects.all()
    if request.method == 'POST':
        classroom_id = request.POST['classroom']
        subject_id = request.POST['subject']
        teacher_id = request.POST['teacher']
        day = request.POST['day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        ClassSchedule.objects.create(
            classroom_id=classroom_id,
            subject_id=subject_id,
            teacher_id=teacher_id,
            day=day,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('manage_schedule')
    return render(request, 'dashboard/manage_schedule.html', {
        'classes': classes,
        'subjects': subjects,
        'teachers': teachers,
        'schedules': schedules,
        'days': DAYS,
    })

@login_required
def view_schedule(request):
    user = request.user
    if user.profile.role == 'teacher':
        schedules = ClassSchedule.objects.filter(teacher=user)
    elif user.profile.role == 'student':
        classrooms = user.classrooms.all()
        schedules = ClassSchedule.objects.filter(classroom__in=classrooms)
    else:
        schedules = ClassSchedule.objects.all()
    return render(request, 'dashboard/view_schedule.html', {'schedules': schedules})

