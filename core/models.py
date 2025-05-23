from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(User, related_name='classrooms', blank=True,
                                      limit_choices_to={'profile__role': 'student'})
    teachers = models.ManyToManyField(User, related_name='teaching_classes', blank=True,
                                      limit_choices_to={'profile__role': 'teacher'})
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name