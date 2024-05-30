from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Branch(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="branches")
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="branch_media", blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    branch = models.ForeignKey(Branch, models.CASCADE, "comments")
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="comment_media", blank=True, null=True)

    def __str__(self):
        return self.content

