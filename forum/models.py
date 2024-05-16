from django.db import models


# Create your models here.

class Branch(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    forum = models.ForeignKey(Branch, models.CASCADE, "comments")
