from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_schedule, name='manage_schedule'),
    path('view/', views.view_schedule, name='view_schedule'),
]