from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="email address")
    first_name = models.CharField(max_length=255, verbose_name="first name")
    last_name = models.CharField(max_length=255, verbose_name="last name")
    is_staff = models.BooleanField(default=False, verbose_name="staff status")

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
