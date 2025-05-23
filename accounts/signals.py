from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Set role according to user type
        if instance.is_superuser:
            Profile.objects.create(user=instance, role='admin')
        elif instance.is_staff:
            Profile.objects.create(user=instance, role='teacher')
        else:
            Profile.objects.create(user=instance, role='student')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()