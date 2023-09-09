from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password


class PersonManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)


class Person(AbstractBaseUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=128, default="default_password")
    biography = models.CharField(max_length=200, null=True)
    photo = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    university = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    invitation_token = models.CharField(
        max_length=255, blank=True, null=True, unique=True
    )
    invitation_expires_at = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "username"

    objects = PersonManager()  # Use the custom manager
