from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.username
