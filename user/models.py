import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class User(AbstractBaseUser):
#     phone = models.CharField("Phone", max_length=20, unique=True)
#     email = models.EmailField("Email", max_length=255, unique=True)
#     username = models.CharField("Username", max_length=35, unique=True, null=True, blank=True)
#     last_login = None
#     first_name = models.CharField('First Name', max_length=255, null=True, blank=True, default='')
#     last_name = models.CharField('Last Name', max_length=255, null=True, blank=True, default='')
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return f"{self.username} {self.id}"

"""
AbstractBaseUser basically provide only 3 fields id, password and last_login
AbstractUser provide 11 all fields and you can add extra fields 
"""


class User(AbstractUser):
    phone = models.CharField("Phone", max_length=20, unique=True)
    email = models.EmailField("Email", max_length=255, unique=True)
    username = models.CharField("Username", max_length=35, unique=True, null=True, blank=True)
    last_login = None
    first_name = models.CharField('First Name', max_length=255, null=True, blank=True, default='')
    last_name = models.CharField('Last Name', max_length=255, null=True, blank=True, default='')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class ToDoTask(models.Model):
    name = models.CharField(max_length=355)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

