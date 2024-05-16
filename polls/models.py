from django.db import models


# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=100)


class Question(models.Model):
    question = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")


class Option(models.Model):
    text = models.TextField()
    answer = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
