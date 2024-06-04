from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    screenshot = models.ImageField(upload_to='project_screenshots/', null = True, blank = True)
    links = models.URLField(null = True, blank = True)
    files = models.FileField(upload_to='project_files/', null = True, blank = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


