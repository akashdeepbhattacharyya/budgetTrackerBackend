from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password

class UserManagementManager(BaseUserManager):
    def create_user(self, userName, password=None, **extra_fields):
        if not userName:
            raise ValueError('The User must have a username')
        user = self.model(userName=userName, **extra_fields)
        user.set_password(password)  # Hash password before saving
        user.save(using=self._db)
        return user

    def create_superuser(self, userName, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(userName, password, **extra_fields)

class UserManagement(AbstractBaseUser, models.Model):
    userName = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManagementManager()

    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.userName

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
