from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Branch(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="branches")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    forum = models.ForeignKey(Branch, models.CASCADE, "comments")
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

