from django.contrib.auth.models import AbstractUser , AbstractBaseUser , PermissionsMixin
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser , PermissionsMixin):
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True , blank=True , null=True )
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    object = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin




