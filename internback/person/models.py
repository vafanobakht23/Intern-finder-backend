from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password

# Create your models here.
# class PersonManager(BaseUserManager):
#     def get_by_natural_key(self, email):
#         return self.get(email=email)

class Person(AbstractBaseUser):
    # username = None
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=128, default='default_password')
    biography = models.CharField(max_length=200,null=True)
    photo = models.CharField(max_length=200,null=True)  # You can also use ImageField if storing images
    invitation_token = models.CharField(
        max_length=255, blank=True, null=True, unique=True
    )
    invitation_expires_at = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    def save(self, *args, **kwargs):
        # Hash the password before saviqng
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    # username = None
    # status  => invited - invitedFailed - active
    # media dir for photo