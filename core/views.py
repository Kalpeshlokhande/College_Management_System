from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile
from core.models import ClassRoom, Subject

@login_required
def dashboard(request):
    role = request.user.profile.role
    if role == 'admin':
        return redirect('admin_dashboard')
    elif role == 'teacher':
        return redirect('teacher_dashboard')
    elif role == 'student':
        return redirect('student_dashboard')
    return render(request, 'base.html')

@login_required
def admin_dashboard(request):
    teachers = Profile.objects.filter(role='teacher')
    students = Profile.objects.filter(role='student')
    classrooms = ClassRoom.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'dashboard/admin_dashboard.html', {
        'teachers': teachers,
        'students': students,
        'classrooms': classrooms,
        'subjects': subjects,
    })

@login_required
def manage_teachers(request):
    teachers = Profile.objects.filter(role='teacher')
    users = User.objects.filter(profile__role='teacher')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            Profile.objects.filter(user=user).update(role='teacher')
        elif action == 'delete':
            user_id = request.POST['user_id']
            User.objects.filter(id=user_id).delete()
        return redirect('manage_teachers')
    return render(request, 'dashboard/manage_teachers.html', {'teachers': teachers, 'users': users})

@login_required
def manage_students(request):
    students = Profile.objects.filter(role='student')
    users = User.objects.filter(profile__role='student')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            Profile.objects.filter(user=user).update(role='student')
        elif action == 'delete':
            user_id = request.POST['user_id']
            User.objects.filter(id=user_id).delete()
        return redirect('manage_students')
    return render(request, 'dashboard/manage_students.html', {'students': students, 'users': users})

@login_required
def manage_subjects(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            name = request.POST['name']
            Subject.objects.create(name=name)
        elif action == 'delete':
            subject_id = request.POST['subject_id']
            Subject.objects.filter(id=subject_id).delete()
        return redirect('manage_subjects')
    return render(request, 'dashboard/manage_subjects.html', {'subjects': subjects})

@login_required
def manage_classes(request):
    classes = ClassRoom.objects.all()
    teachers = User.objects.filter(profile__role='teacher')
    students = User.objects.filter(profile__role='student')
    subjects = Subject.objects.all()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            name = request.POST['name']
            classroom = ClassRoom.objects.create(name=name)
            teacher_ids = request.POST.getlist('teachers')
            student_ids = request.POST.getlist('students')
            subject_ids = request.POST.getlist('subjects')
            classroom.teachers.set(User.objects.filter(id__in=teacher_ids))
            classroom.students.set(User.objects.filter(id__in=student_ids))
            classroom.subjects.set(Subject.objects.filter(id__in=subject_ids))
        elif action == 'delete':
            class_id = request.POST['class_id']
            ClassRoom.objects.filter(id=class_id).delete()
        return redirect('manage_classes')
    return render(request, 'dashboard/manage_classes.html', {
        'classes': classes,
        'teachers': teachers,
        'students': students,
        'subjects': subjects,
    })
@login_required
def manage_teachers(request):
    teachers = Profile.objects.filter(role='teacher')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            Profile.objects.filter(user=user).update(role='teacher')
        elif action == 'delete':
            user_id = request.POST['user_id']
            User.objects.filter(id=user_id).delete()
        return redirect('manage_teachers')
    return render(request, 'dashboard/manage_teachers.html', {'teachers': teachers})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import ClassRoom, Subject
from django.contrib.auth.models import User

# If you want to use ClassSchedule and DAYS
try:
    from schedule.models import ClassSchedule, DAYS
except ImportError:
    ClassSchedule = None
    DAYS = []

@login_required
def manage_schedule(request):
    if ClassSchedule is None:
        return render(request, 'dashboard/manage_schedule.html', {'error': 'Schedule model not found.'})
    classes = ClassRoom.objects.all()
    subjects = Subject.objects.all()
    teachers = User.objects.filter(profile__role='teacher')
    schedules = ClassSchedule.objects.all().order_by('day', 'start_time')
    if request.method == 'POST':
        classroom_id = request.POST.get('classroom')
        subject_id = request.POST.get('subject')
        teacher_id = request.POST.get('teacher')
        day = request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        if classroom_id and subject_id and teacher_id and day and start_time and end_time:
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