from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    imege = models.ImageField(upload_to='announcements/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)