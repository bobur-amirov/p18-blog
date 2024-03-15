from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import UserManager


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    username = None

    USERNAME_FIELD = 'phone'
    objects = UserManager()

