from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    nickname = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=True)
