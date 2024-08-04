# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from main.models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
    else:
        # Update the profile if it already exists
        profile, created = Profile.objects.get_or_create(user=instance)
        profile.save()
