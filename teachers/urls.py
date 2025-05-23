from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('assignments/', views.teacher_assignments, name='teacher_assignments'),
    path('announcements/', views.teacher_announcements, name='teacher_announcements'),
]