from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField("auth.Permission")

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username