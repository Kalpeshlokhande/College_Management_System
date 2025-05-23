from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('assignments/', views.view_assignments, name='student_assignments'),
]