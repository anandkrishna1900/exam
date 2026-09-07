from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

# a Post belongs to one user (foreign key relationship)
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
