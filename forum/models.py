from django.db import models


# Create your models here.

class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Branch(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    forum = models.ForeignKey(Forum, models.CASCADE, "branches")
