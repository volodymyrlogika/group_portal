from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    screenshots = models.ImageField(upload_to='')
    links = models.URLField()
    files = models.FileField(upload_to='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    

class CustomUser(AbstractUser):
    portfolio_description = models.TextField(blank=True)

    def __str__(self):
        return self.username



class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_create_portfolio = models.BooleanField(default=False)
    can_edit_portfolio = models.BooleanField(default=False)
    can_delete_portfolio = models.BooleanField(default=False)

    def __str__(self):
        return f"Permissions for {self.user.username}"




