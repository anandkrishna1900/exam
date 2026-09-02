from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # extra custom fields beyond Django's built-in user
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
