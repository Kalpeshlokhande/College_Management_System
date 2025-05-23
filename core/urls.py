from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-teachers/', views.manage_teachers, name='manage_teachers'),
    path('manage-students/', views.manage_students, name='manage_students'),
    path('manage-classes/', views.manage_classes, name='manage_classes'),
    path('manage-subjects/', views.manage_subjects, name='manage_subjects'),
    path('manage-schedule/', views.manage_schedule, name='manage_schedule'),
]
urlpatterns += [
    path('manage-teachers/', views.manage_teachers, name='manage_teachers'),
    path('manage-students/', views.manage_students, name='manage_students'),
    path('manage-classes/', views.manage_classes, name='manage_classes'),
    path('manage-subjects/', views.manage_subjects, name='manage_subjects'),
]