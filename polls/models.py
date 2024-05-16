from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="polls")

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=500)
    max_points = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")


class Option(models.Model):
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")


class UserPollResult(models.Model):
    completed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_polls_results")
    poll = models.ForeignKey(Poll, on_delete=models.DO_NOTHING, related_name="poll_results")
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)
