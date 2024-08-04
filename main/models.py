from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin/Researcher'),
        ('user', 'Regular User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class NLPProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class NLPEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='research_papers/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

