from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        return self.create_user(email, password, **kwargs)

    def create_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
